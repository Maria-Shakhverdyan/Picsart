ls = [ ]
n = int(input("Enter the size of the array: "))
count = 0

while(count < n):
    element = int(input("Enter the element: "))
    ls.append(element)
    count += 1

if n > 0:
    max_num_index = 0
    min_num_index = 0

    for i in range(1, len(ls)):
        if ls[i] > ls[max_num_index]:
            max_num_index = i
        if ls[i] < ls[min_num_index]:
            min_num_index = i
            
    sub = max_num_index - min_num_index
    print(sub)    
        
else:
    print("the array is empty")