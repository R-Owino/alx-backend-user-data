#!/usr/bin/env python3
"""
This module contains a class SessionAuth that inherits from Auth.
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id
        Args:
            user_id (str): User ID to associate with the Session ID
        Returns:
            - If user_id is None, return None
            - Otherwise, return the Session ID
        """
        if user_id is None or type(user_id) != str:
            return None

        # generate session_id using uuid4()
        session_id = str(uuid.uuid4())

        # store user_id in the dictionary associated with session_id
        self.user_id_by_session_id[session_id] = user_id

        return session_id
