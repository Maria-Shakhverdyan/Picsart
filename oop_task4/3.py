class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Invalid input type")
        self.__celsius = value

    @property
    def celsius_to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32

temp = Temperature(25)
print(temp.celsius_to_fahrenheit)

temp.celsius = 40
print(temp.celsius_to_fahrenheit)

try:
    temp.celsius = "a"
    print(temp.celsius_to_fahrenheit)
except TypeError as e:
    print(e)