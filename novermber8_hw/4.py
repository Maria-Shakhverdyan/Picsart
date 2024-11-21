import json

'''Problem: You are given a JSON file user_data.json containing user profiles.
Write a program to load the data, filter users based on specific criteria (e.g., age over 30 and role is “manager”),
and output the filtered data to a new JSON file called filtered_users.json.'''

def load_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def filter_data(users, age_criteria, role_criteria):
    filtered = []
    for user in users:
        if user['age'] > age_criteria and user['role'] == role_criteria:
            filtered.append(user)
    return filtered
    
def update_data(filtered_users, filename):
    with open(filename, 'w') as new_file:
        json.dump({'users':filtered_users}, new_file, indent=4)
        
if __name__ == '__main__':
    data = load_data('user_data.json')
    
    filtered_users = filter_data(data['users'], 30, 'manager')
    
    update_data = update_data(filtered_users, 'new_user_data.json')
    
    print("Filtered users have been saved to 'new_user_data.json'.")