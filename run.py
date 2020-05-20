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

def create_credentials(application_name, account_username, account_password):
    new_credentials = Credentials(application_name, account_username, account_password)
    return new_credentials

def display_credentials():
    return Credentials.display_credentials()

def credentials_exist(application_name):
    return Credentials.credentials_exist(application_name)

def main():
    print("PASSWORD LOCKER")
    print("--"*30)
    print("An application that manages your passwords.")
    print("\n")
    print("What is your name?")
    current_user = input()
    print("\n")
    print(f"Hello {current_user}. Are you a new user or would you like to create an account")
    print("\n")

    while True:
                    print("Use these short codes : CC - create an account , SI - sign into an existing account , EX -exit the application ")

                    short_code = input().upper()

                    if short_code == 'CC':
                        print("CREATE AN ACCOUNT")
                        print("-"*10)

                        print("Enter a name you wish to use as your username")
                        print("*the username must contain alphabetical letters only*")
                        
                        while True:
                            username = input()
                            if username.isalpha():
                                print("Enter a password for your account")
                                print("*the password must be 6 characters or longer*")
                                while True:
                                    login_password = input()
                                    if len(login_password) >= 6:
                                        add_user(create_user(username, login_password))
                                        print(f"Account for {username} created. Proceed to log in.")
                                    else:
                                        print("The password you entered is too short.")
                                        print("Please use a password of 6 characters or more")
                                        continue

                            else:
                                print("The username you entered is not valid.")
                                print("Please use alphabetical letters only")
                                continue
                    
                    elif short_code == 'EX':
                            print("Bye....")
                            break
                

if __name__ == '__main__':

    main()