  from data import prices, recipes
  class Finances:
    def __init__(self):
      self.budget = 0

    def change_bugdet(self, number):
      self.budget = int(number)

    def price_of_recipe(self, key):
      price = 0
      for i in range(0, len(recipes[key])):
        price += prices[recipes[key][i]]
      return price

    def find_recipes_available(self):
      recipes_available = []
      for key in recipes:
        if self.price_of_recipe(key) <= self.budget:
          recipes_available.append(key)
      return recipes_available


