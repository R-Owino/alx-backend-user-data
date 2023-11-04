#!/usr/bin/env python3
"""
Module that contains a function filter_datum
"""

import re
import logging
import os
from typing import List
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Function that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = None):
        """ Constructor method for RedactingFormatter class """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Method that filters values in incoming log records using filter_datum.
        Values for fields in fields should be filtered
        """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Method that takes no arguments and returns a logging.Logger object.
    The logger should be named "user_data" and only log up to logging.INFO
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    sh = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Method that returns a connector to the database
    """
    return mysql.connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'root'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME', 'my_db'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME', 'localhost'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', 'root'),
    )


def main():
    """
    Main function
    Fetches users from the database and prints them
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        message = f"name={row[0]}; " + \
                  f"email={row[1]}; " + \
                  f"phone={row[2]}; " + \
                  f"ssn={row[3]}; " + \
                  f"password={row[4]}; " + \
                  f"ip={row[5]}; " + \
                  f"last_login={row[6]}; " + \
                  f"user_agent={row[7]};"
        logger.info(message)


if __name__ == "__main__":
    print(main())
