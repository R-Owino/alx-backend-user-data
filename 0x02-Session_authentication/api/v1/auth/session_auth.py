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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID

        Args:
            session_id (str): The Session ID

        Returns:
            - If session_id is None or no user_id is linked to session_id,
              return None
            - Otherwise, return the User ID linked to session_id
        """
        if session_id is None or type(session_id) != str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value
        """
        cookie_name = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie_name)
        from models.user import User
        return User.get(user_id)
