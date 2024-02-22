from models.menu.dish import MenuItem


class Drink(MenuItem):

    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return self._name

    def discount(self):
        self._price -= (self._price * 0.8)
