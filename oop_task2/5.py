class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_in_stock = quantity_in_stock

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_quantity_in_stock(self, quantity):
        if quantity >= 0:
            self.__quantity_in_stock = quantity
        else:
            raise ValueError("Count cannot be negative")

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_quantity_in_stock(self):
        return self.__quantity_in_stock

    def add_stock(self, amount):
        if amount > 0:
            self.__quantity_in_stock += amount
            print(f"{amount} added, current -> {self.__quantity_in_stock}")
        else:
            raise ValueError("Count must be positive")

    def reduce_stock(self, amount):
        if 0 <= amount <= self.__quantity_in_stock:
            self.__quantity_in_stock -= amount
            print(f"{amount} deleted, current -> {self.__quantity_in_stock}")
        else:
            raise ValueError("You cannot delete more items than you have in stock.")

try:
    product = Product(1, "Backpack", 5)
    product.add_stock(5)
    product.reduce_stock(3)

    print(f"Current -> {product.get_quantity_in_stock()}")

    product.reduce_stock(20)
except ValueError as e:
    print("Error :", e)
