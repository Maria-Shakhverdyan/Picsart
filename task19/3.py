def fact(number):
    if number <= 1:
        return 1
    else:
        return number + (fact(number - 1))
    
number = int(input("Enter the number: "))
result = fact(number)

print(result)
