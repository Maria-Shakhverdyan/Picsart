class PasswordValidator:
    def __init__(self, min_length=8, must_contain_digit=True,
                 must_contain_upper=True, must_contain_lower=True,
                 must_contain_special=True, cannot_contain_space=True):
        self.min_length = min_length
        self.must_contain_digit = must_contain_digit
        self.must_contain_upper = must_contain_upper
        self.must_contain_lower = must_contain_lower
        self.must_contain_special = must_contain_special
        self.cannot_contain_space = cannot_contain_space
        self.password = None

    def __get__(self, instance, owner):
        return self.__password

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string.")
        
        if len(value) < self.min_length:
            raise ValueError(f"Password must be at least {self.min_length} characters long.")
        
        if self.must_contain_digit and not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit.")
        
        if self.must_contain_upper and not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter.")
        
        if self.must_contain_lower and not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter.")
        
        if self.must_contain_special and not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in value):
            raise ValueError("Password must contain at least one special character.")
        
        if self.cannot_contain_space and " " in value:
            raise ValueError("Password cannot contain spaces.")
        
        self.__password = value

class Account:
    password = PasswordValidator(min_length=8)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"Account(username: {self.username})"


try:
    acc = Account("john_doe", "Pass123!")
    print(acc)

    acc.password = "short"
except ValueError as e:
    print(e)

try:
    acc.password = "password" 
except ValueError as e:
    print(e)

try:
    acc.password = "Pass123"  
except ValueError as e:
    print(e)

try:
    acc.password = "Pass 123!" 
except ValueError as e:
    print(e)

try:
    acc.password = "PASSWORD123!"
except ValueError as e:
    print(e)

try:
    acc.password = "pass123!"
except ValueError as e:
    print(e)

try:
    acc.password = "ValidPass123!"
    print(f"Password set successfully: {acc.password}")
except ValueError as e:
    print(e)
