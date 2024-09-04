class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, {self.name} !!!")
    
    def print_atributes(self):
        print(f"The name is: {self.name}, the age is: {self.age}")


person1 = Person("Maria", "21")

person1.greet()
person1.print_atributes()