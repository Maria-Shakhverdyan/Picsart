from typing import List
from abc import ABC, abstractmethod

class Course:
    def __init__(self, instructor: 'Professor', name, content):
        self.instructor = instructor
        self.name = name
        self.content = content
        self.students: List['Student'] = []
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def instructor(self):
        return self.__instructor

    @instructor.setter
    def instructor(self, value):
        if not isinstance(value, Professor):
            raise TypeError("Instructor must be a Professor")
        self.__instructor = value
    
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError("Content must be a string")
        if value == "":
            raise ValueError("Content cannot be empty")
        self.__content = value
    
    def add_student(self, student):
        self.students.append(student)
        student.enrolled_courses.append(self)
    
    def remove_student(self, student):
        self.students.remove(student)
        student.enrolled_courses.remove(self)
    
    def course_info(self):
        return f"Course: {self.name}, Instructor: {self.instructor.name}, Content: {self.content}"


class Student:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.enrolled_courses: List[Course] = []
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError("Contact info must be a string")
        if value == "":
            raise ValueError("Contact info cannot be empty")
        self.__contact_info = value
    
    def enroll(self, course: Course):
        course.add_student(self)
    
    def view_progress(self):
        print(f"{self.name}'s Enrolled Courses:")
        for course in self.enrolled_courses:
            print(course.course_info())

class Professor:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError("Contact info must be a string")
        if value == "":
            raise ValueError("Contact info cannot be empty")
        self.__contact_info = value
    
    def create_course(self, name, content):
        return Course(self, name, content)
    
    def manage_course(self, course: Course):
        print(f"Managing course: {course.course_info()}")

class CourseType(ABC):
    @abstractmethod
    def course_level_info(self):
        pass

class UndergraduateCourse(CourseType):
    def course_level_info(self):
        return "Course Level: Undergraduate"

class GraduateCourse(CourseType):
    def course_level_info(self):
        return "Course Level: Graduate"

class Assignment(ABC):
    @abstractmethod
    def submit(self):
        pass
    
    @abstractmethod
    def grade(self):
        pass

professor = Professor("Dr. John Smith", "john.smith@university.edu")
course1 = professor.create_course("Introduction to Python", "Learn the basics of Python programming.")
course2 = professor.create_course("Advanced Python", "Deep dive into Python programming.")
student1 = Student("Maria Sh", "maria.sh@email.com")
student1.enroll(course1)
student1.enroll(course2)
student1.view_progress()
professor.manage_course(course1)
professor.manage_course(course2)
print(course1.course_info())
print(course2.course_info())
