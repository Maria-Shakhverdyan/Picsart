from abc import ABC, abstractmethod

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.medical_history = []
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value == "":
            raise ValueError
        self.__name = value
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.__age = value
    
    def add_medical_history(self, value):
        self.medical_history.append(value)
    
    def view_medical_history(self):
        return self.medical_history

class Doctor:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value == "":
            raise ValueError
        self.__name = value

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value == "":
            raise ValueError
        self.__contact_info = value
    
    def manage_patient_info(self, patient: Patient):
        ...

    def schedule_appointment(self, patient: Patient):
        ...

class MedicalStaff(ABC):
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value == "":
            raise ValueError
        self.__name = value
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value == "":
            raise ValueError
        self.__position = value
    
    def manage_operations(self):
        ...

class MedicalProcedure(ABC):
    @abstractmethod
    def perform(self):
        pass


class Surgery(MedicalProcedure):
    def perform(self):
        return "Surgery performed"


class CheckUp(MedicalProcedure):
    def perform(self):
        return "Check-up done"


patient = Patient("Maria Sh", 21)
doctor = Doctor("Dr. Smith", "smith@example.com")
staff = MedicalStaff("Nurse Anna", "Nurse")

patient.add_medical_history("Grip 2023-01-01")
print(patient.view_medical_history())

doctor.schedule_appointment(patient)
staff.manage_operations()

surgery = Surgery()
print(surgery.perform())
    
checkup = CheckUp()
print(checkup.perform())