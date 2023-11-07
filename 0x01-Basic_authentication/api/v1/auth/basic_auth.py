#!/usr/bin/env python3
"""
This module contains a class BasicAuth that inherits from Auth.
"""

from api.v1.auth.auth import Auth


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
