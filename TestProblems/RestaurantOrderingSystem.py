from abc import ABC, abstractmethod
from typing import List

class Dish(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value <= 0:
            raise ValueError("Price must be positive")
        self.__price = value

    @abstractmethod
    def dish_info(self):
        pass

class Appetizer(Dish):
    def dish_info(self):
        return f"The dish -> {self.name}, the price -> {self.price}"

class Entree(Dish):
    def dish_info(self):
        return f"The dish: {self.name}, the price: {self.price}"

class Menu:
    def __init__(self):
        self.dishes: List[Dish] = []
    
    def add_dish(self, dish):
        self.dishes.append(dish)

    def show_menu(self):
        print("Menu: ")
        for dish in self.dishes:
            print(dish.dish_info())

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history: List['Order'] = []
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError("Contact info must be a string")
        if value == "":
            raise ValueError("Contact info cannot be empty")
        self.__contact_info = value
    
    def view_menu(self, menu: Menu):
        return menu.show_menu()
    
    def place_order(self, dishes: List[Dish]):
        order = Order(self, dishes)
        self.order_history.append(order)
    
    def view_order_history(self):
        print("Order history: ")
        for order in self.order_history:
            print(order.order_info())

class Order:
    def __init__(self, customer: Customer, dishes_ordered: List[Dish]):
        self.customer = customer
        self.dishes_ordered = dishes_ordered
        self.total_price = sum(dish.price for dish in dishes_ordered)
    
    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError("Customer must be a Customer object")
        self.__customer = value
    
    def order_info(self):
        ordered_dishes = ", ".join(dish.name for dish in self.dishes_ordered)
        return f"Order by {self.customer.name}: Dishes: {ordered_dishes}, Total Price: {self.total_price}"

if __name__ == "__main__":
    menu = Menu()

    appetizer1 = Appetizer("Pomidorov dzvadzex", 5.99)
    entree1 = Entree("Khorovats", 15.99)
    menu.add_dish(appetizer1)
    menu.add_dish(entree1)

    customer = Customer("Maria", "maria@example.com")

    customer.view_menu(menu)

    customer.place_order([appetizer1, entree1])

    customer.view_order_history()
