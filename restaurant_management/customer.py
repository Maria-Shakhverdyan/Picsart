class Customer:
    __slots__ = ('name', 'contact_info', 'order_history')

    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []
    
    def place_order(self, order):
        self.order_history.append(order)

    def view_order_history(self):
        return self.order_history

    def display_info(self):
        return f"The customer is {self.name}, contact info is {self.contact_info}, order history {self.order_history}."