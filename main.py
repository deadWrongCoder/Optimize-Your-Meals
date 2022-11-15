'''Optimize Your Meals
taking finances, health, time and food preferences into account'''

prices = {
  "bread": 50,
  "potato": 10,
  "tomato": 30,
  "cucumber": 15,
  "meat": 200,
  "milk": 60
  }
recipes = {
  "simple salad": ["tomato", "cucumber"],
  "simple garnish": ["potato", "milk"],
  "main course": ["meat", "potato", "milk"]
}

def price_of_recipe(key):
  price = 0
  for i in range(0, len(recipes[key])):
    price += prices[recipes[key][i]]
  return price
  
def find_recipes_available(bugdet_per_meal):
  recipes_available = []
  for key in recipes:
    if price_of_recipe(key) <= bugdet_per_meal:
      recipes_available.append(key)
  return recipes_available
  
def find_tasty_recipes(food_preferences):
  recipes_available = []
  for key in recipes:
    if food_preferences in recipes[key]:
      pass
    else:  
      recipes_available.append(key)
  return recipes_available
  

budget = int(input("What's your budget per meal? "))
food_preferences = input("What's the product do you hate the most? ")
budget_list = find_recipes_available(budget)
tasty_list = find_tasty_recipes(food_preferences)
result = [value for value in budget_list if value in tasty_list]
print(", ".join(result))
  
