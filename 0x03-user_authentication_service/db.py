#!/usr/bin/env python3
"""
DB module
Note: DB._session is a private property and hence should NEVER
be used from outside the DB class
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> None:
        """Add a user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user by arbitrary keyword arguments

        Returns:
            the first row in the users table as filtered
            by the method's input arguments

        Raises:
            - InvalidRequestError: if the keyword arguments are
            not mapped onto the users table
            - NoResultFound: if the query selects no rows
        """
        if not kwargs:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user
