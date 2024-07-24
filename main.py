#!/usr/bin/env python3
"""
Main file
"""
from models.auth import Auth

email = 'bos2ab@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

print(auth.create_session(email))
print(auth.create_session("unknown@email.com"))