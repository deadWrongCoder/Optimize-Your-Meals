'''Optimize Your Meals
taking finances, health, time and food preferences into account'''

from finances import Finances
from preferences import Preferences


user_finances = Finances()
user_preferences = Preferences()

user_finances.change_bugdet()
user_preferences.change_preferences()
budget_list = user_finances.find_recipes_available()
tasty_list = user_preferences.find_tasty_recipes()
result = [value for value in budget_list if value in tasty_list]
print(", ".join(result))
