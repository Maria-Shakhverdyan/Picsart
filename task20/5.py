def maximum(num1 = 0, num2 = 0, num3 = 0):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
for i in range(3):
    number = int(input(f"Enter the {i+1} number: "))
print(maximum(number))

print(maximum(1, 5, 10))
print(maximum(1, 5, 3))
