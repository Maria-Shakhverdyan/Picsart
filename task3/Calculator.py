def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("ZeroDivision error.")
    else:
        return x / y

def calculator():
    print("Choose the operation: ")
    print("1. Add: ")
    print("2. Subtract: ")
    print("3. Multiply: ")
    print("4. Divide: ")
    
    while True:
        choise = (input("Choose 1/2/3/4: "))
    
        if choise in ['1', '2', '3', '4']:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
        
            if choise == '1':
                print(f"{a} + {b} = {add(a, b)}")
            elif choise == '2':
                print(f"{a} - {b} = {subtract(a, b)}")
            elif choise == '3':
                print(f"{a} * {b} = {multiply(a, b)}")
            else:
                print(f"{a} / {b} = {divide(a, b)}")
                
            next_calculation = input("Do you want to continue? Yes/No: ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Wrong command")
            
calculator()
