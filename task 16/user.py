reserved_names = ['admin', 'root']

# Username
while True:
    username = input("Enter username: ")
    if not (5 <= len(username) <= 20):
        print("Username must be between 5 and 20 characters long.")
    elif not username.isalnum():
        print("Username can only contain alphanumeric characters.")
    elif username.lower() in reserved_names:
        print("Username cannot be a reserved name.")
    else:
        break

# Email
while True:
    email = input("Enter email: ")
    if "@" not in email or "." not in email or email.startswith('@') or email.endswith('@') or email.startswith('.') or email.endswith('.'):
        print("Invalid email format.")
    else:
        break

# Phone Number
while True:
    phone = input("Enter phone number: ")
    if not (phone.startswith("+374") and len(phone) == 12 and phone[1:].isdigit()) and not (phone.startswith("0") and len(phone) == 9 and phone.isdigit()):
        print("Invalid phone number format.")
    else:
        break

# Password
while True:
    password = input("Enter password: ")
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
    elif not any(char in '!@#$%^&*' for char in password):
        print("Password must contain at least one special character.")
    else:
        break

# Password Repeat
while True:
    password_repeat = input("Repeat password: ")
    if password != password_repeat:
        print("Passwords do not match.")
    else:
        break

print("Registration data is valid.")
