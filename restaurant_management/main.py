from menu_items import MenuItem
from order import TakeawayOrder, DineInOrder, DeliveryOrder
from customer import Customer

appetizer = MenuItem('Akroshka', 5.99, ['matsun', 'varung', 'kanachi'])
entree = MenuItem('khorovats', 20.99, ['xozi mis', 'havi mis', 'sous'])
dessert = MenuItem('ptichi', 6.99, ['kat', 'kakao'])

customer = Customer('Maria', 'maria@example.com')

dine_in_order = DineInOrder(customer, [appetizer, entree, dessert], table_number=5)
print(f"Dine-in order total: ${dine_in_order.total_price:.2f}")
print(dine_in_order.place_order())

takeaway_order = TakeawayOrder(customer, [entree], time='18:00')
print(f"Takeaway order total: ${takeaway_order.total_price:.2f}")
print(takeaway_order.place_order())

delivery_order = DeliveryOrder(customer, [appetizer, dessert], address='123 Main St', fee=3.50)
print(f"Delivery order total: ${delivery_order.total_price:.2f}")
print(delivery_order.place_order())

print(appetizer.display_info()) # Name: Akroshka, Price: $5.99, Ingredients: matsun, varung, kanachi
print(entree.display_info())    # Name: khorovats, Price: $20.99, Ingredients: xozi mis, havi mis, sous
print(dessert.display_info())   # Name: ptichi, Price: $6.99, Ingredients: kat, kakao
