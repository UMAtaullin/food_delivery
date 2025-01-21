from file_reader import read_menu
from menu import menu


def get_order():
  order = {}
  order['name'] = input("Enter your name: ")
  drinks = read_menu("drinks.txt")
  dishes = read_menu("dishes.txt")
  garnishes = read_menu("garnishes.txt")
  
  order['drink'] = menu(drinks, "Elon's delivery drinks:", "Choose your drink:")
  order['dish'] = menu(dishes, "Elon's delivery dishes:", "Choose your dish:")
  order['garnish'] = menu(garnishes, "Elon's delivery garnishes:", "Choose your garnish:")
  
  return order

