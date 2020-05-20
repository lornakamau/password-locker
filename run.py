#!/usr/bin/env python3.6
from users import Users
from credentials import Credentials

def create_user(username, login_password):
    new_user = Users(username, login_password)
    return new_user
    