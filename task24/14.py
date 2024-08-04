def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Try div to zero.")
    return a / b

calc_dict = {
        '+' : add,
        '-' : sub,
        '*' : mul,
        '/' : div
    }

def calculate(op1, op2, operator):
    if operator not in calc_dict:
        raise ValueError("Chka senc operator")
    oper_func = calc_dict[operator]

    return oper_func(op1, op2)

try:
    print("Add:", calculate(5, 3, '+'))  # Outputs: 8
    print("Sub:", calculate(5, 3, '-'))  # Outputs: 2
    print("Mul:", calculate(5, 3, '*'))  # Outputs: 15
    print("Div:", calculate(5, 3, '/'))  # Outputs: 1.666...
    print("Div:", calculate(5, 0, '/'))  # ZeroDivisionError
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
except Exception as e:
    print("An unexpected error occurred:", e)