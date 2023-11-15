#!/usr/bin/env python3
"""
This module contains the SQLAlchemy model for a database table
named users
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# create declarative_base instance
Base = declarative_base()


class User(Base):
    '''
    SQLAlchemy model for a database table named users

    Columns:
        id (Integer): unique user id
        email (String): user email address
        hashed_password (String): user password
        session_id (String): user session id
        reset_token (String): user reset token
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
