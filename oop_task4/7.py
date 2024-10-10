class RangeDescriptor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.value = None
    
    def __get__(self, instance, owner):
        return self.__value
    
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be number.")
        if value < self.min_value or value > self.max_value:
            raise ValueError("Value must be between min_value and max_value.")
        self.__value = value

class Product:
    price = RangeDescriptor(0, 100)

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

try:
    prod1 = Product("Laptop", 50)
    print(prod1)

    prod2 = Product("Smartphone", 120)
except ValueError as e:
    print(e)

try:
    prod1.price = "a"
except ValueError as e:
    print(e)