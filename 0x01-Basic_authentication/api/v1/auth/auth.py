#!/usr/bin/env python3
"""
This module contains a class Auth
"""

import fnmatch
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manages API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Args:
            - path: path to check
            - excluded_paths: list of paths that do not need authentication
        Returns:
          - True if path is not in the list of strings excluded_paths
        """
        if path is None or excluded_paths is None or excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        # for excluded_path in excluded_paths:
        #     if fnmatch.fnmatch(path, excluded_path):
        #         return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Args:
            - request: Flask request object
        Returns:
          - The value of the header request Authorization
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns:
          - None
        """
        return None
