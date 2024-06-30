ls1 = [ ]
n1 = int(input("Enter the size of the first array: "))
count1 = 0

while(count1 < n1):
    element = int(input("Enter the element: "))
    ls1.append(element)
    count1 += 1

ls2 = [ ]
n2 = int(input("Enter the size of the second array: "))
count2 = 0

while(count2 < n2):
    element = int(input("Enter the element: "))
    ls2.append(element)
    count2 += 1
    
if ls1 == ls2:
    print("equal")
else:
    print("not equal")