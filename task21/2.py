def calculate_total_price(*item_prices, tax_rate = 0.08):
    subtotal = sum(item_prices)
    tax = subtotal * tax_rate
    total_price = subtotal + tax
    return total_price

result_1 = calculate_total_price(100, 100)
print("The result_1 is: ", result_1)

result_2 = calculate_total_price(20, 20, tax_rate = 0.2)
print("The result_2 is: ", result_2)