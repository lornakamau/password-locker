#!/usr/bin/env python3.6
from users import Users
from credentials import Credentials

def create_user(username, login_password):
    new_user = Users(username, login_password)
    return new_user

def add_user(user):
    user.add_user()

def delete_user(user):
    user.delete_user()

def find_user(username):
    return Users.find_by_username(username)

def check_existing_user(username):
    return Users.user_exists(username)