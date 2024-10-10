class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a positive integer.")
        if value > 100:
            raise ValueError("Age must be 100 or less.")
        self.__age = value
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = value


person1 = Person("Maria", 21)
print(person1.name, person1.age)

person1.age = 40
person1.name = "Ann"
print(person1.name, person1.age)

try:
    person1.age = -5
except ValueError as e:
    print(e)
