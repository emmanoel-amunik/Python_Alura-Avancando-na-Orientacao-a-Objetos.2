from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish


restaurant_square = Restaurant("square", "Gourmet")

drink_juice = Drink("Watermelon Juice", 5.0, "big")
dish_bread = Dish("Bread", 2.0, "The best bread in the city")


def main():
    print(drink_juice)
    print(dish_bread)


if __name__ == "__main__":
    main()
