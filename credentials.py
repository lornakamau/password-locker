class Credentials:
    credentials_list = []

    def __init__ (self, application_name, account_username, account_password):
        self.application_name = application_name
        self.account_username = account_username
        self.account_password = account_password