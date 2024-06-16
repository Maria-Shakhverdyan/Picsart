count = int(input("Enter the count of elements in list: "))
ls = []

for i in range(count):
    element = int(input(f"Enter element {i + 1}: "))
    ls.append(element)
    
number = int(input("Enter the number: "))
    
if number in ls:
    print("Yes")
else:
    print("No")