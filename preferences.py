from data import recipes


class Preferences:
    def __init__(self):
        self.hated_products = []
        self.favourite_products = []

    def change_preferences(self, hated_products):
        self.hated_products.extend(hated_products.split(", "))

    def find_tasty_recipes(self):
        recipes_available = []
        deleted_recipes = []
        for key in recipes:
            recipes_available.append(key)

        for i in range(0, len(self.hated_products)):
            for key, value in recipes.items():
                if self.hated_products[i] in value and key not in deleted_recipes:
                    recipes_available.remove(key)
                    deleted_recipes.append(key)

        return recipes_available

