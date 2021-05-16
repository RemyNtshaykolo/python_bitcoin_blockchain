from user import User


class Transaction:
    def __init__(self, sender: User, receiver: User, amount: float):
        self.__sender: User = sender
        self.__receiver: User = receiver
        self.__amount: float = amount

    def __str__(self):
        return "{}_{}_{}".format(
            self.__sender.name, self.__receiver.name, str(self.__amount)
        )

    @property
    def sender(self):
        return self.__sender

    @property
    def receiver(self):
        return self.__receiver

    @property
    def amount(self):
        return self.__amount
