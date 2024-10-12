class MenuItem:
    __slots__ = ('name', 'price', 'ingredients')
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
    
    def display_info(self):
        return f"Name: {self.name}, Price: ${self.price:.2f}, Ingredients: {', '.join(self.ingredients)}"


class Appetizer(MenuItem):
    __slots__ = ('spicy_level')
    
    def __init__(self, name, price, ingredients, spicy_level):
        super().__init__(name, price, ingredients)
        self.spicy_level = spicy_level
    
class Entree(MenuItem):
    __slots__ = ('serving_size')
    def __init__(self, name, price, ingredients, serving_size):
        super().__init__(name, price, ingredients)
        self.serving_size = serving_size

class Dessert(MenuItem):
    __slots__ = ('sweetness_level')
    def __init__(self, name, price, ingredients, sweetness_level):
        super().__init__(name, price, sweetness_level)
        self.sweetness_level = sweetness_level