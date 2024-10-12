#incorrect
#The Employee class is responsible for both calculating salaries and generating reports.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def generate_report(self):
        report = f"Employee: {self.name}, Salary: {self.salary}"
        print(report)
        return report

#correct
# We will divide the responsibilities into two separate classes: one for calculating payroll, one for generating reports.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class SalaryCalculator:
    def calculate_salary(self, employee):
        return employee.salary

class ReportGenerator:
    def generate_report(self, employee):
        report = f"Employee: {employee.name}, Salary: {employee.salary}"
        print(report)
        return report
