class Users:
    users_list = []

    def __init__ (self, username, login_password):
        self.username = username
        self.login_password = login_password
    
    def add_user(self):
        Users.users_list.append(self)

    def delete_user(self):
        Users.users_list.remove(self)