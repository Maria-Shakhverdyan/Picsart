ls = []
n = int(input("Enter the list size: "))  # Поправил текст запроса на ввод

count = 0

while count < n:
    element = int(input("Enter the element: "))
    ls.append(element)
    count += 1

try:
    if len(ls) == 0:
        raise IndexError("Clear from empty list")
    
    ls[:] = []
    print(ls)
except IndexError as e:
    print(f"An error occurred: {e}")
