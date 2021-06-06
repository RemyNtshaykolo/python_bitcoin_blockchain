from typing import Dict, List
from transaction import Transaction
import logging as log


class Block:
    def __init__(self, hash_previous_block: str, balance_book: Dict[str, float] = {}):
        self._previous_block_hash = hash_previous_block
        self._transactions_book = []
        self._accounts_book: Dict[str, float] = balance_book

    @property
    def accounts_book(self):
        return self._accounts_book

    @property
    def transactions_book(self):
        return self._transactions_book

    def add_public_key_to_accounts_book(self, public_key: str, balance=0):
        """
        Add a new public key to the accounts books with a the given balance
        """
        self._accounts_book[public_key] = balance

    def add_transaction_order(self, transaction: Transaction):
        """
        Add a transaction order the transaction books
        """
        self._transactions_book.append(transaction)

    def check_public_key_solvency(self, public_key: str, amount: float) -> bool:
        """
        Check that the public key is solvent for the given amount
        """
        pbk_balance = self.accounts_book[public_key]
        return pbk_balance >= amount

    def check_public_key_existence(self, public_key: str) -> bool:
        """
        Check that the public key is part of the account book
        """
        return public_key in self._accounts_book

    def verify_block(self):
        """
        Verify the integrity of each transactions within a block.
        To do so, verify that the sender and the receiver public key exist into the accounts book
        then verify the sender solvency
        """
        incorrect_transactions: List[Transaction] = []
        balance_book_copy: Dict[str, float] = self._accounts_book.copy()
        tx: Transaction
        for tx in self._transactions_book:
            sender_pbk = tx.sender.public_key
            receiver_pbk = tx.receiver.public_key

            log.info("Checking transaction {}".format(tx))
            receiver_exist = self.check_public_key_existence(receiver_pbk)
            sender_exist = self.check_public_key_existence(sender_pbk)
            sender_solvency = self.check_public_key_solvency(sender_pbk, tx.amount)

            if not receiver_exist & sender_exist & sender_solvency:
                incorrect_transactions.append(tx)
            balance_book_copy[sender_pbk] = balance_book_copy[sender_pbk] - tx.amount
            balance_book_copy[receiver_pbk] = balance_book_copy[receiver_pbk] + tx.amount

    @property
    def length(self):
        return len(self._transactions_book)

    # @property
    # def hash(self):
    #     log.info("Hashing block content")
    #     stacked_transactions_book = "\n".join([tx.__str__() for tx in self._transactions_book])
    #     block_payload = (self.__previous_block_hash + stacked_transactions_book).encode()
    #     return SHA256(block_payload).hexdigest()[:5]
