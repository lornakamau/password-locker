class Users:
    users_list = []

    def __init__ (self, username, login_password):
        self.username = username
        self.login_password = login_password
    
    def add_user(self):
        Users.users_list.append(self)

    def delete_user(self):
        Users.users_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        for user in Users.users_list:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls, username):
        for user in Users.users_list:
            if user.username == username:
                return True
        return False