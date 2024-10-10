class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a number (int or float).")
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Height must be a number (int or float).")
        if value <= 0:
            raise ValueError("Height must be a positive number.")
        self.__height = value

    @property
    def area(self):
        return self.__width * self.__height
    
    @property
    def perimeter(self):
        return 2 * (self.__width * self.__height)
    
rect = Rectangle(5, 10)
print(f"Width: {rect.width}, Height: {rect.height}")
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")

# Change values
rect.width = 7
rect.height = 3
print(f"Updated Area: {rect.area}")
print(f"Updated Perimeter: {rect.perimeter}")