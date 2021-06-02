from unittest import TestCase
from unittest.mock import MagicMock, patch
from .transaction import Transaction
from .user import User


class UserTest(TestCase):
    def test_encryption(self):
        print("hello")
