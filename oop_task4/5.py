class ValidatedString:
    def __init__(self, name, min_length):
        self.name = name
        self.min_length = min_length

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Sxal type")
        if len(value) < self.min_length:
            raise ValueError("Petqa lini gone min_length-i chap")
        instance.__dict__[self.name] = value

class User:
    username = ValidatedString("Username", min_length = 5)

    def __init__(self, username):
        self.username = username

user1 = User("Maria")
print(user1.username)

try:
    user2 = User("")
    user2.name = 13
except Exception as e:
    print(e)
