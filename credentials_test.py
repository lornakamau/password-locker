import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.new_credentials = Credentials("Twitter", "cirukamau", "lol")

    def test_initialization(self):
        self.assertEqual(self.new_credentials.application_name, "Twitter")
        self.assertEqual(self.new_credentials.account_username, "cirukamau")
        self.assertEqual(self.new_credentials.account_password, "lol")