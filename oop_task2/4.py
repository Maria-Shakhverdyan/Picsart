class ShoppingCart:
    def __init__(self):
        self.__items = []
    
    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__items.append({"name": name, "price": price})
        print(f"Item {name} added to list with price -> {price:.2f}")


    def remove_item(self, name):
        for item in self.__items:
            if item["name"] == name:
                self.__items.remove(item)
                print(f"Item {name} removed from list")
                return
            
        print(f"Item {name} not find.")

    def total_items(self):
        return len(self.__items)
    
    def display_cart(self):
        if not self.__items:
            print("Empty list.")
        else:
            print("Items in list:")
            for item in self.__items:
                print(f"Name: {item['name']}, Price: {item['price']:.2f}")

cart = ShoppingCart()
cart.add_item("Xndzor", 2)
cart.add_item("Tandz", 1.5)
cart.display_cart()
print(f"Count of items: {cart.total_items()}\n")

cart.remove_item("Xndzor")
cart.display_cart()
print(f"Count of items: {cart.total_items()}")