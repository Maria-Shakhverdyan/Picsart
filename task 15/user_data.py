users_dict = {}
users_list = []

def add_user(user_id, first_name, last_name, email, password, phone):
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

def find_user_by_name(first_name):
    result = [user for user in users_list if user['first_name'] == first_name]
    if result:
        return result
    else:
        return "Not found"

def import_user_data():
    user_id = input("Enter user_id: ")
    first_name = input("Enter first_name: ")
    last_name = input("Enter last_name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    phone = input("Enter phone: ")
    add_user(user_id, first_name, last_name, email, password, phone)

while True:
    action = input("Select action: \n[1] Import user data \n[2] Find user by name \n[3] Exit\n")
    if action == '1':
        import_user_data()
    elif action == '2':
        name_to_search = input("Enter first_name for search: ")
        found_users = find_user_by_name(name_to_search)
        print("Found users: ", found_users)
    elif action == '3':
        break
    else:
        print("Incorrect password, try again.")
