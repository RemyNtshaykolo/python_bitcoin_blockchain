from __future__ import annotations
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User


class Transaction:
    def __init__(self, sender: "User", receiver: "User", amount: float):
        self.__sender: "User" = sender
        self.__receiver: "User" = receiver
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
        return "{}_send_{}_to_{}".format(
            self.__sender,
            self.__amount,
            self.__receiver,
        )

    @property
    def encoded(self):
        return str(self).encode()

    def is_signed(self):
        """Check if a transaction if signed. Return False if not and True otherwise"""
        return self.__signature is not None

    def sign(self, private_key):
        """
        Generate the transaction signature from a private key
        """
        self.__signature = private_key.sign(
            self.encoded,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )

    def verify(self):
        """
        Verify that the transaction match its signature
        """
        self.__sender.public_key.verify(
            self.__signature,
            self.encoded,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256(),
        )
