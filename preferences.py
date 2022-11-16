from data import recipes

class Preferences:
  def __init__(self):
    self.hated_products = []
    self.favourite_products = []

  def change_preferences(self):
    hated_products = input("What's the product do you hate the most? ")
    self.hated_products.append(hated_products)
    

  def find_tasty_recipes(self):
    recipes_available = []
    for key in recipes:
      if self.hated_products[0] in recipes[key]:
        pass
      else:  
        recipes_available.append(key)
    return recipes_available
