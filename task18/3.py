def print_list(my_list):
    if len(my_list) == 0:
        print("The list is empty")
    else:
        for i in my_list:
            print(i)


count = 0
my_list = []
n = int(input("Enter the number: "))

while count < n:
    element = int(input(f"Enter the {count + 1} element: "))
    my_list.append(element)
    count += 1

print_list(my_list)