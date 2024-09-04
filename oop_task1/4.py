class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def greet(self):
        print(f"Hello, {self.name} !!!")
    
    def print_atributes(self):
        print(f"The name is: {self.name}, the age is: {self.__age}")
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age.")



person1 = Person("Maria", 21)

person1.print_atributes()

person1.greet()

current_age = person1.get_age()
print(f"Current age is: {current_age}")

person1.set_age(25)

person1.print_atributes()

person1.set_age(-5)
