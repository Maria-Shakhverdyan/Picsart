import random

users_dict = {}
users_list = []

def generate_user_id():
    return ''.join(random.choices('1234567890', k=6))

def add_user():
    user_id = generate_user_id()
    first_name = input("Enter first_name: ")
    last_name = input("Enter last_name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    phone = input("Enter phone: ")

    user = {
        'id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'phone': phone
    }

    users_dict[user_id] = user
    users_list.append(user)

def find_user_by_name():
    name_to_search = input("Enter first_name for search: ")
    found_users = [user for user in users_list if user['first_name'] == name_to_search]
    if found_users:
        print("Found users: ", found_users)
    else:
        print("Not found")

while True:
    action = input("Select action: \n[1] Import user data \n[2] Find user by name \n[3] Exit\n")
    if action == '1':
        add_user()
    elif action == '2':
        find_user_by_name()
    elif action == '3':
        break
    else:
        print("Incorrect option, please try again.")
