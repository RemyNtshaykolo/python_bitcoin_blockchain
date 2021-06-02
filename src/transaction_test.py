from unittest import TestCase
from .transaction import Transaction
from .user import User
from cryptography.exceptions import InvalidSignature


class TransactionTest(TestCase):
    def test_transaction(self):
        """Sign a transaction with a user, and then verify it with another user"""
        john = User("john")
        marie = User("marie")
        transaction = Transaction(john, marie, 20)
        john.sign_transaction(transaction)
        marie.verify_transaction(transaction)

    def test_corrupted_transaction(self):
        """
        Try to modify the transaction after it has been signed.
        When the verification is made, then an error should ne raised.
        """
        john = User("john")
        marie = User("marie")

        transaction = Transaction(john, marie, 20)
        john.sign_transaction(transaction)

        transaction.amount = 100000
        with self.assertRaises(InvalidSignature):
            marie.verify_transaction(transaction)
        transaction = Transaction(john, marie, 20)
