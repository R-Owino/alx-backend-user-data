#!/usr/bin/env python3
"""
This module contains a class SessionDBAuth that inherits from SessionExpAuth
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class
    """

    def create_session(self, user_id=None):
        """
        Creates and stores new instance of UserSession

        Returns:
            - Session ID
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        kwargs = {
            'user_id': user_id,
            'session_id': session_id
        }
        user_session = UserSession(**kwargs)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Requests UserSession in the database based on session_id

        Returns:
            - User ID based on a Session ID
        """
        if session_id is None:
            return None

        UserSession.load_from_file()
        user_session = UserSession.search({'session_id': session_id})

        if not user_session:
            return None

        if self.session_duration <= 0:
            return user_session[0].user_id

        if 'created_at' not in user_session[0].__dict__:
            return None

        time_now = datetime.now()
        duration = timedelta(seconds=self.session_duration)

        if time_now > user_session[0].created_at + duration:
            return None

        return user_session[0].user_id

    def destroy_session(self, request=None):
        """
        Destroys UserSession based on the session ID from
        the request cookie

        Returns:
            - True if session ID for the user is successfully deleted
            - False if request is None or if cookie is not found
        """
        session_id = self.session_cookie(request)
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False

        if not sessions:
            return False

        sessions[0].remove()
        return True
