import math

def area_of_circle(radius):
    return math.pi * radius ** 2

def area_of_square(side):
    return side ** 2

def area_of_rectangle(width, height):
    return width * height

def area_of_triangle(base, height):
    return 0.5 * base * height

object_oper = {
    'circle': area_of_circle,
    'square': area_of_square,
    'rectangle': area_of_rectangle,
    'triangle': area_of_triangle
}

def calculate_area(shape, **kwargs):
    if shape not in object_oper:
        raise ValueError("Chka senc operacia")
    area_func = object_oper[shape]
    return area_func(**kwargs)

try:
    print("The area of circle is: ", calculate_area('circle', radius = 5))
    print("The area of suqare is: ", calculate_area('square', side = 10))
    print("The area of rectangle is: ", calculate_area('rectangle', width = 10, height = 5))
    print("The area of triangle is: ", calculate_area('triangle', base = 10, height = 10))
    print("The area of triangle is: ", calculate_area('esim e', base = 10, height = 10))

except ValueError as e:
    print(e)