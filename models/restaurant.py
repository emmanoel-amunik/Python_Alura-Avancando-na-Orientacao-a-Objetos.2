from models.rating import Rating
from models.menu.menu_item import MenuItem


class Restaurant:

    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._activate = False
        self._rating = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self._category}"

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    @classmethod
    def list_restaurants(cls):

        print(f"{'Name'.ljust(27)} {'Category'.ljust(27)} {'Rating'.ljust(27)}"
              f"{'Status'}\n")

        for restaurant in cls.restaurants:
            print(f"{restaurant.get_name().ljust(25)} | "
                  f"{restaurant.get_category().ljust(25)} | "
                  f"{str(restaurant.rating_average).ljust(25)} | "
                  f"{restaurant.activate}")

    @property
    def activate(self):
        return "true" if self._activate else "false"

    def change_status(self):
        self._activate = not self._activate

    def collect_rating(self, client, grade):

        if 0 < grade < 5:
            rating = Rating(client, grade)
            self._rating.append(rating)

    @property
    def rating_average(self):

        if not self._rating:
            return "-"

        grades_sum = sum(rating._grade for rating in self._rating)
        grades_quantity = len(self._rating)
        average = round(grades_sum / grades_quantity, 1)

        return average

    def menu_add(self, item):

        if isinstance(item, MenuItem):
            self._menu.append(item)
        else:
            raise ValueError("Invalid item")

    @property
    def display_menu(self):

        print(f"Restaurant {self._name} Menu\n")

        for index, item in enumerate(self._menu, start=1):

            if hasattr(item, "description"):
                dish_message = (f"{index}. Name: {item._name} | "
                                f"Price: ${item._price} | "
                                f"Description: {item.description}")
                print(dish_message)

            elif hasattr(item, "size"):
                drink_message = (f"{index}. Name: {item._name} | "
                                 f"Price: ${item._price} | "
                                 f"Size: {item.size}")
                print(drink_message)
