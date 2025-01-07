from get_order import get_order


def print_order(order):
  print("Here is your order, ", order["name"])
  print("Drinks: ", order["drink"])
  print("Dish: ", order["dish"])
  print("Garnish: ", order["garnish"])
  print("Thanks for your order!")
  return

order = get_order()
print_order(order)