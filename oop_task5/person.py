class Person:
    __slots__ = ('name', 'age', 'email')
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def display_info(self):
        return f"Name: {self.name}, age: {self.age}, email: {self.email}."


person1 = Person("Maria", 21, "maria@gmail.com")
print(person1.display_info())

try:
    person1.phone = "094278040"
except AttributeError as e:
    print(e)
