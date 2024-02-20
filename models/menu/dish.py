from models.menu.menu_item import MenuItem


class Dish(MenuItem):

    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return self._name
