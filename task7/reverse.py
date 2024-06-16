count = int(input("Enter the count of elements in list: "))
original_ls = []

for i in range(count):
    element = input(f"Enter element {i + 1}: ")
    original_ls.append(element)
    
original_ls.reverse()
reversed_ls = original_ls

print(reversed_ls)
