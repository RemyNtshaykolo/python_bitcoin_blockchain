from abc import ABC, abstractmethod


class Blockchain(ABC):
    """
    Template of a blockchain
    """

    @abstractmethod
    def add_transaction(self):
        pass