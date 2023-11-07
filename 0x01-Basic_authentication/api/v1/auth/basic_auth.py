#!/usr/bin/env python3
"""
This module contains a class BasicAuth that inherits from Auth.
"""

from base64 import b64decode
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVarap    


class BasicAuth(Auth):
    """ BasicAuth class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Args:
            - authorization_header: string representing the value of an
            authorization header
        Returns:
            - Base64 part of the authorization header for
            a basic authentication
        """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        Args:
            - base64_authorization_header: string representing the value of a
            base64 authorization header
        Returns:
            - decoded value of a Base64 string base64_authorization_header
        """
        if base64_authorization_header is None or \
                type(base64_authorization_header) != str:
            return None
        try:
            return b64decode(base64_authorization_header,
                             validate=True).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        Args:
            - decoded_base64_authorization_header: string representing the
            decoded value of a base64 authorization header
        Returns:
            - the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) != str or \
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Args:
            - user_email: string representing the user email
            - user_pwd: string representing the user password
        Returns:
            - User instance based on his email and password
        """
        if user_email is None or type(user_email) != str or \
                user_pwd is None or type(user_pwd) != str:
            return None
        users = User.search({'email': user_email})
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
