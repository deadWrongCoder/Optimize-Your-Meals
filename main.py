'''Optimize Your Meals
taking finances, health, time and food preferences into account'''

from finances import Finances
from preferences import Preferences
from tkinter import *


def generate_dishes():
    user_finances = Finances()
    user_preferences = Preferences()
    user_finances.change_bugdet(budget_entry.get())
    user_preferences.change_preferences(preferences_entry.get())
    budget_list = user_finances.find_recipes_available()
    tasty_list = user_preferences.find_tasty_recipes()
    result = [value for value in budget_list if value in tasty_list]
    result_label.config(text=", ".join(result))

window = Tk()
window.geometry("500x500")
budget_label = Label(text = "What's your budget per meal?" )
preferences_label = Label(text = "What are the products you hate the most? ")
result_label = Label(text="Sample")
budget_entry = Entry()
budget_entry.insert(0, "0")
preferences_entry = Entry()
generate_button = Button(text="Generate list of dishes", command = generate_dishes)
budget_label.pack(padx=10, pady=10)
budget_entry.pack(padx=10, pady=10)
preferences_label.pack(padx=10, pady=10)
preferences_entry.pack(padx=10, pady=10)
generate_button.pack(padx=10, pady=10)
result_label.pack(padx=10, pady=10)
window.mainloop()
