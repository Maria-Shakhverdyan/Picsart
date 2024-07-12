def find_max(my_list):
    max_num = my_list[0]
    for i in range(1, len(my_list)):
        if i > max_num:
            max_num = my_list[i]
    return(max_num)

def find_min(my_list):
    min_num = my_list[0]
    for i in range(1, len(my_list)):
        if i < min_num:
            min_num = my_list[i]
    return min_num

count = 0
my_list = []
n = int(input("Enter the number: "))

while count < n:
    element = int(input(f"Enter the {count + 1} element: "))
    my_list.append(element)
    count += 1

print("The maximum element is: ", find_max(my_list))
print("The minimum element is: ", find_min(my_list))