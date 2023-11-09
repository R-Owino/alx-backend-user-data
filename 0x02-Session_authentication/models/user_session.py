#!/usr/bin/env python3
"""
This module contains a model UserSession that inherits from Base
"""

from models.base import Base


class UserSession(Base):
    """ UserSession class """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a user session instance """

        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        self.email = kwargs.get('email')
        self._password = kwargs.get('_password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
