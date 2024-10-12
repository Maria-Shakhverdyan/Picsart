from abc import ABC, abstractmethod
    
class Order(ABC):
    __slots__ = ('customer', 'menu_items', 'total_price')
    
    def __init__(self, customer, menu_items, total_price):
        self.customer = customer
        self.menu_items = menu_items
        self.total_price = self.calculate_total()
    
    @abstractmethod
    def place_order(self):
        ...
    
    def calculate_total(self):
        return sum(item.price for item in self.menu_items)  

class DineInOrder(Order):
    __slots__ = ('table_number')

    def __init__(self, customer, menu_items, table_number):
        super().__init__(customer, menu_items, total_price=None)
        self.table_number = table_number

    def place_order(self):
        return f"Order placed for table {self.table_number}."
    
class TakeawayOrder(Order):
    __slots__ = ('time')

    def __init__(self, customer, menu_items, time):
        super().__init__(customer, menu_items, total_price=None)
        self.time = time

    def place_order(self):
        return f"Takeaway order placed, pick-up time: {self.time}."


class DeliveryOrder(Order):
    __slots__ = ('address', 'fee')

    def __init__(self, customer, menu_items, address, fee):
        super().__init__(customer, menu_items, total_price=None)
        self.address = address
        self.fee = fee
        self.total_price += fee

    def place_order(self):
        return f"Delivery order placed to address: {self.address}."