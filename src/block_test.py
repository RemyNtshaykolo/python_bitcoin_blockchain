from unittest import TestCase
from unittest.mock import Mock
from block import Block


class TestBlock(TestCase):
    def setUp(self) -> None:
        self.block = Block("hash")

    def test_add_public_key_to_accounts_book(self):
        self.assertFalse(self.block.accounts_book)
        self.block.add_public_key_to_accounts_book("pbk_1")
        self.assertDictEqual(self.block.accounts_book, {"pbk_1": 0})

    def test_add_transaction_order(self):
        self.assertFalse(self.block.transactions_book)
        TransactionMock = Mock()
        tx = TransactionMock()
        self.block.add_transaction_order(tx)
        self.assertListEqual(self.block.transactions_book, [tx])

    def test_check_public_key_solvency(self):
        self.block.add_public_key_to_accounts_book("pbk_1", 10)
        self.assertTrue(self.block.check_public_key_solvency("pbk_1", 10))
        self.assertTrue(self.block.check_public_key_solvency("pbk_1", 10))
        self.assertFalse(self.block.check_public_key_solvency("pbk_1", 11))

    def test_check_public_key_existence(self):
        self.assertFalse(self.block.check_public_key_existence("pbk_1"))
        self.block.add_public_key_to_accounts_book("pbk_1", 10)
        self.assertTrue(self.block.check_public_key_existence("pbk_1"))
