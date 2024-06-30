n = int(input("Enter count of elements in list: "))
ls = []

count = 0

while count < n:
    element = int(input("Enter the element: "))
    ls.append(element)
    count += 1
    
index = int(input("Enter index: "))
num = int(input("Enter the num: "))

for i in range(len(ls)):
    if i == index:
        ls[i] = num
        break
        
print(ls)
    
