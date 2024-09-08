class Student:
    def __init__(self, name, roll_number):
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            raise ValueError("The grade must be between 0 and 100.")
    
    def average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        else:
            return 0
    
    def display_info(self):
        avg_grade = self.average()
        print(f"Student -> {self.__name}, roll number -> {self.__roll_number}, grade -> {self.__grades}, average -> {avg_grade:.2f}.")


try:
    student = Student("Maria", 101)
    student.add_grade(85)
    student.add_grade(90)
    student.add_grade(78)
    
    student.display_info()

    student.add_grade(105)
except ValueError as e:
    print("Error: ", e)