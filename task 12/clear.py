ls = []
n = int(input("Enter the list: "))
count = 0

while count < n:
    element = (int(input("Enter the element: ")))
    ls.append(element)
    count += 1

if len(ls) == 0:
    raise IndexError("Clear from empty list")

ls[:] = []

print(ls)