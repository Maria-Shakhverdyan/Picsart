def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def square_root(number):
    return number ** 0.5

def factorial(number):
    return 1 if number <= 1 else number * factorial(number - 1)

math_opers = {
    'square' : square,
    'cube' : cube,
    'square_root' : square_root,
    'factorial' : factorial
}

def math_operations(number, operation):
    if operation not in math_opers:
        raise ValueError("Chka senc operacia")
    math_func = math_opers[operation]
    return math_func(number)

number = int(input("Enter the number: "))

try:
    print(f"The square of {number} is: ", square(number))
    print(f"The cube of {number} is: ", cube(number))
    print(f"The square_root of {number} is: ", square_root(number))
    print(f"The factorial of {number} is: ", factorial(number))
except ValueError as e:
    print(e)