class Descriptor:
    def __get__(self, instance, owner):
        return instance.__dict__.get('score', 0)
    
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Invalid value type.")
        if value < 0 or value > 100:
            raise ValueError("Score must be between 0 and 100.")
        
        instance.__dict__['score'] = value

class Student:
    score = Descriptor()

    def __init__(self, name, score):
        self.name = name
        self.score = score 

student1 = Student("Maria", 85)
print(student1.name)
print(student1.score) #85

student1.score = 95
print(student1.score) #95

try:
    student1.score = 150
except ValueError as e:
    print(e)