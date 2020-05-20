import unittest
from users import Users

class TestUsers(unittest.TestCase):

    def setUp(self):
        self.new_user = Users("Lorna", "97")

    def test_initialization(self):
        self.assertEqual(self.new_user.username, "Lorna")
        self.assertEqual(self.new_user.login_password, "97")