from typing import List
from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
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
            raise TypeError("Price must be number")
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self.__price = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("Description must be a string")
        if value == "":
            raise ValueError("Description cannot be empty")
        self.__description = value

    def product_info(self):
        return f"Product name: {self.name}, price: {self.price}, description: {self.description}"

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history: List[Order] = []
    
    def add_order(self, order):
        self.order_history.append(order)
    
    def show_order_history(self):
        history = []
        for order in self.order_history:
            products_info = [f"{product.name} (${product.price})" for product in order.products]
            total = order.calculate_total()
            history.append(f"Order: {', '.join(products_info)} | Total: ${total}")
        return history


class Order:
    def __init__(self, customer: Customer, products: List[Product]):
        self.customer = customer
        self.products = products
        self.total_price = self.calculate_total()
    
    def calculate_total(self):
        return sum(product.price for product in self.products)

class ProductType(ABC):
    @abstractmethod
    def show_product_type(self):
        pass

class Electronics(ProductType):
    def show_product_type(self):
        return "Books"

class Clothing(ProductType):
    def show_product_type(self):
        return "Clothing"

product1 = Product("Pride & Prejudice", 25, "Book about love")
product2 = Product("Hoodie", 20, "White hoodie")

customer1 = Customer("Maria", "maria@example.com")

order1 = Order(customer1, [product1, product2])
customer1.add_order(order1)

print(customer1.show_order_history())
