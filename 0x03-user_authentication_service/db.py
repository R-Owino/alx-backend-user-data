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
        self._engine = create_engine("sqlite:///a.db", echo=False)
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

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a user to the database through sqlalchemy session

        Args:
            email (str): user email
            hashed_password (str): user hashed password

        Returns:
            user object created
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

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates a user's attributes in the DB

        Args:
            user_id (int): user id
            kwargs (dict): key/value pairs to update user attributes

        Raises:
            ValueError: if user_id is not linked to any user object in the DB
            ValueError: if any of kwargs keys are not attibutes of the User
            class
        """
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if k not in user.__dict__:
                raise ValueError
            setattr(user, k, v)
        self._session.commit()
        return None
