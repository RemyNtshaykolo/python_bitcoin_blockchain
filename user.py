from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend
from uuid import uuid4


class User:
    def __init__(self, name: str):
        self.__create_key_pair()
        self.__name = name
        self.__id = uuid4()

    def __create_key_pair(self):
        key = rsa.generate_private_key(
            backend=crypto_default_backend(), public_exponent=65537, key_size=2048
        )
        self.__private_key = key.private_bytes(
            crypto_serialization.Encoding.PEM,
            crypto_serialization.PrivateFormat.PKCS8,
            crypto_serialization.NoEncryption(),
        )
        self.__public_key = key.public_key().public_bytes(
            crypto_serialization.Encoding.OpenSSH,
            crypto_serialization.PublicFormat.OpenSSH,
        )

    @property
    def public_key(self):
        return self.__public_key.decode()

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id
