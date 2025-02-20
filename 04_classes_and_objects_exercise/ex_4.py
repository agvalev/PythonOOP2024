class PizzaDelivery:
    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return self.pizza_already_ordered_message()

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0

        self.ingredients[ingredient] += quantity
        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return self.pizza_already_ordered_message()

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):
        if self.ordered:
            return self.pizza_already_ordered_message()
        
        self.ordered = True
        formated_ingredients = [f"{ing}: {quantity}" for ing, quantity in self.ingredients.items()]
        return (f"You've ordered pizza {self.name} "
                f"prepared with {', '.join(formated_ingredients)} and the price will be {self.price}lv.")

    def pizza_already_ordered_message(self):
        return f"Pizza {self.name} already prepared, and we can't make any changes!"


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})

margarita.add_extra('mozzarella', 1, 0.5)

margarita.add_extra('cheese', 1, 1)

margarita.remove_ingredient('cheese', 1, 1)

print(margarita.remove_ingredient('bacon', 1, 2.5))

print(margarita.remove_ingredient('tomatoes', 2, 0.5))

margarita.remove_ingredient('cheese', 2, 1)

print(margarita.make_order())

print(margarita.add_extra('cheese', 1, 1))