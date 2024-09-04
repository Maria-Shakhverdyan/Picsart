class Person:
    name = "esim"
    age = 0
    
    def print_atributes(self):
        print(f"The name is: {self.name}, the age is: {self.age}")

person1 = Person()
person1.name = "Maria"
person1.age = 21

person1.print_atributes()