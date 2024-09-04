class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_atributes(self):
        print(f"The name is: {self.name}, the age is: {self.age}")

person1 = Person("Maria", "21")

person1.print_atributes()