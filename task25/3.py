def validate_positive_integers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                raise ValueError("arg is not positive")
            
        for key, value in kwargs.items():
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Value is not positive")
            
        return func(*args, **kwargs)
    
    return wrapper


@validate_positive_integers
def add(a, b):
    return a + b

@validate_positive_integers
def div(a, b):
    return a // b

@validate_positive_integers
def square(a):
    return a ** 2

@validate_positive_integers
def sub(a, b):
    return a - b if a > b else b - a

print("The result of add: ", add(4, 5))
print("The result of div: ", div(5, 4))
print("The result of square: ", square(4))
print("The result of sub: ", sub(4, 8))
print("The result of add: ", add(4, 0))