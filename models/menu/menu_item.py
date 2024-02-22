from abc import ABC
from abc import abstractmethod


class MenuItem(ABC):

    def __init__(self, name, price):
        self._name = name
        self._price = price

    @abstractmethod
    def discount(self):
        pass