class Descriptor:
    def __init__(self, max_salary):
        self.salary = None
        self.max_salary = max_salary

    def __get__(self, instance, owner):
        if self.__salary is None:
            raise AttributeError("Attribute not found")
        return self.__salary

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be number")
        if value > self.max_salary:
            raise ValueError("Value must be less than max_salary")
        if value < 0:
            raise ValueError("Value must be positive.")
        self.__salary = value
    
class Employee:
    salary = Descriptor(max_salary=2000)

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

try:
    emp1 = Employee("Alice", 1000)
    print(emp1)

    emp2 = Employee("Bob", 3000)
except ValueError as e:
    print(e)

try:
    emp1.salary = -10_000
except ValueError as e:
    print(e)
