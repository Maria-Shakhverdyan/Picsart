def display_product_details(name, price, category, stock):
    print(f"Product name: {name}")
    print(f"Product price: ${price: .2f}")
    print(f"Product category: {category}")
    print(f"Product stock: {stock}")

product_info = {
    'name': 'Copybook',
    'price': 2.5,
    'category': 'BackToSchool',
    'stock': '25',
}

display_product_details(**product_info)