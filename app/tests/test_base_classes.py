import unittest

from app.models import users, user_status

from constants import (
    post_marios,
    post_status
)


class TestUser(unittest.TestCase):
    
    def setUp(self) -> None:
        # Initialize a new `users.Users` object for each `TestUser.<test_method>`.
        self.test_user = users.Users(**post_marios)
    
    def test_init_users(self):
        # Test `users.Users()` object (implicit from `setUp`).
        self.assertIsInstance(self.test_user, users.Users)
    
    def test_user_attributes(self):
        # Loads `self.test_user` locally
        test_user = self.test_user
        # Loop over global config dictionary
        for key, value in post_marios.items():
            # Get current attribute $key from test_user(users.Users) object
            _test_attr = getattr(test_user, key)
            # Test all instances return string types
            self.assertIsInstance(_test_attr, str)
            self.assertEqual(_test_attr, value)
    
    def tearDown(self) -> None:
        # Clear `users.Users` object from current namespace.
        # Called after every successful `TestUser.<test_method>`
        del self.test_user


class TestUserStatus(unittest.TestCase):
    
    def setUp(self) -> None:
        self.test_status = user_status.UserStatus(**post_status)
    
    def test_init_user_status(self):
        self.assertIsInstance(self.test_status, user_status.UserStatus)
    
    def test_user_status_attributes(self):
        # Loads `self.test_user` locally
        test_user = self.test_status
        # Loop over global config dictionary
        for key, value in post_status.items():
            # Get current attribute $key from test_user(users.Users) object
            _test_attr = getattr(test_user, key)
            # Test all instances return string types
            self.assertIsInstance(_test_attr, str)
            self.assertEqual(_test_attr, value)
    
    def tearDown(self) -> None:
        del self.test_status
