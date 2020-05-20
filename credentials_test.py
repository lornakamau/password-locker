import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.new_credentials = Credentials("Twitter", "cirukamau", "lol")

    def test_initialization(self):
        self.assertEqual(self.new_credentials.application_name, "Twitter")
        self.assertEqual(self.new_credentials.account_username, "cirukamau")
        self.assertEqual(self.new_credentials.account_password, "lol")

    def tearDown(self):
        Credentials.credentials_list = []

    def test_add_multiple_credentials(self):
        self.new_credentials.add_credentials()
        test_credentials = Credentials("Instagram", "Alfred", "101")
        test_credentials.add_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        self.new_credentials.add_credentials()
        test_credentials = Credentials("Instagram", "Alfred", "101")
        test_credentials.add_credentials()

        test_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_display_all_credentials(self):
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)