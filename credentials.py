class Credentials:
    credentials_list = []

    def __init__ (self, application_name, account_username, account_password):
        self.application_name = application_name
        self.account_username = account_username
        self.account_password = account_password

    def add_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        return Credentials.credentials_list

    @classmethod
    def find_by_application_name(cls, application_name):
        for credential in Credentials.credentials_list:
            if credential.application_name == application_name:
                return credential
    
    @classmethod
    def credentials_exist(cls, application_name):
        for credential in Credentials.credentials_list:
            if credential.application_name == application_name:
                return True
        return False
    