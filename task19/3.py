def summa(number):
    if number == 0:
        return 0
    else:
        return number + (summa(number - 1))
    
number = int(input("Enter yhe number: "))
result = summa(number)

print(result)