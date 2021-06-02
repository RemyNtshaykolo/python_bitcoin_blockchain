from transaction import Transaction
from blockchain import Blockchain
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend


from uuid import uuid4


class User:
    def __init__(self, name: str):
        self.__create_key_pair()
        self.__name = name
        self.__id = uuid4()

    def __str__(self):
        return self.name

    def __create_key_pair(self):
        self.__private_key = rsa.generate_private_key(
            backend=crypto_default_backend(), public_exponent=65537, key_size=2048
        )
        self.__public_key = self.__private_key.public_key()

    @property
    def public_key(self):
        return self.__public_key

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def sign_transaction(self, transaction: Transaction):
        """
        Sign transaction using private key
        """
        transaction.sign(self.__private_key)

    def verify_transaction(self, transaction: Transaction):
        transaction.verify()

    def make_transaction(self, amount: float, receiver, blockchain: Blockchain):
        transaction: Transaction = Transaction(self, receiver, amount)
        transaction.sign(self.__private_key)
