def division(x, y):
    if x + y == 0:
        print("ZeroDivisionError")
    else:
        return (x - y) / (x + y)
        
a = float(input("Input x: "))
b = float(input("Input y: "))

#call function
result = division(a, b)
print("The result is: ", result)