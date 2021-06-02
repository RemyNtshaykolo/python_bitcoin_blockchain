from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from .user import User


class Transaction:
    def __init__(self, sender: User, receiver: User, amount: float):
        self.__sender: User = sender
        self.__receiver: User = receiver
        self.__amount: float = amount
        self.__signature = None

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    def __str__(self):
        """Return a string representation of a transaction"""
        return "{} send {} to {}".format(
            self.__sender,
            self.__amount,
            self.__receiver,
        )

    def is_signed(self):
        """Check if a transaction if signed. Return False if not and True otherwise"""
        return self.__signature is not None

    def sign(self, private_key):
        """
        Generate the transaction signature from a private key
        """

        formated_transaction = "{}_{}_{}".format(
            self.__sender.name, self.__receiver.name, str(self.__amount)
        )
        self.__signature = private_key.sign(
            formated_transaction.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )

    def verify(self):
        """
        Verify that the transaction match its signature
        """
        formated_transaction = "{}_{}_{}".format(
            self.__sender.name, self.__receiver.name, str(self.__amount)
        )
        self.__sender.public_key.verify(
            self.__signature,
            formated_transaction.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
