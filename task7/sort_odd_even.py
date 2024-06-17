count = int(input("Enter the count of elements: "))
ls = []

for i in range(count):
    number = int(input("Enter the string: "))
    ls.append(number)
    
even = []
odd = []

for number in ls:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
        
ls = even + odd
print(ls)
        