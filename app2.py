from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish


restaurant_square = Restaurant("square", "Gourmet")

drink_juice = Drink("Watermelon Juice", 5.0, "big")
dish_bread = Dish("Bread", 2.0, "The best bread in the city")

drink_juice.discount()
dish_bread.discount()

restaurant_square.menu_add(drink_juice)
restaurant_square.menu_add(dish_bread)


def main():
    restaurant_square.display_menu


if __name__ == "__main__":
    main()
