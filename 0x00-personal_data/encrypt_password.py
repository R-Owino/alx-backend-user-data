#!/usr/bin/env python3
"""
Module that contains a function hash_password
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function that takes in a password string arguments and returns a salted,
    hashed password, which is a byte string.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
