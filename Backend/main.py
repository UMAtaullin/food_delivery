from menu import menu
from file_reader import read_menu
from get_order import get_order

def main():
    list_drinks = read_menu("drinks.txt")
    list_dishes = read_menu("dishes.txt")
    list_garnish = read_menu("garnishes.txt")
    
    drinks = menu(list_drinks, "Elon's delivery drinks:", "Choose your drink:")
    dishes = menu(list_dishes, "Elon's delivery dishes:", "Choose your dish:")
    garnishes = menu(list_garnish, "Elon's delivery garnishes:", "Choose your garnish:")

    print("\nHere is your order:")
    print(f"Drink: {drinks}")
    print(f"Dish: {dishes}")
    print(f"Garnish: {garnishes}")
    print("Thanks for your order!")

if __name__ == "__main__":
    main()
