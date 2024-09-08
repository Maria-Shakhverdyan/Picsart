class Employee:
    def __init__(self, employee_id, name, salary):
        self.setId(employee_id)
        self.setName(name)
        self.setSalary(salary)
    
    def getId(self):
        return self.__employee_id
    
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def setId(self, employee_id):
        self.__employee_id = employee_id
    
    def setName(self, name):
        self.__name = name
    
    def setSalary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            raise ValueError("Salary value cannot be negative")
        

employee = Employee(101, "Maria", 5000)

employee.setSalary(6000)

try:
    employee.setSalary(-1000)
except ValueError as e:
    print("Error: ", e)

print("The salary is: ", employee.getSalary())

try:
    employee.setSalary(5000)
except ValueError as e:
    print(e)

print("The user id is: ", employee.getId())
print("The name of user is: ", employee.getName())
print("The salary of user is: ", employee.getSalary())
