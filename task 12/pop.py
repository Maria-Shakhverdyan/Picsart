ls = []
n = int(input("Enter the list: "))
count = 0

while count < n:
    element = (int(input("Enter the element: ")))
    ls.append(element)
    count += 1

# tarberak 1
try:
    if len(ls) == 0:
        raise IndexError("pop from empty list")
except IndexError as e:
    print(f"An error occurred: {e}")
    exit()

new = []    
for i in ls:
    if(i != ls[-1]):
        new.append(i)


print(ls[-1])
print("The final list: ", new)


# tarberak 2

# try:
#     if len(ls) == 0:
#         raise IndexError("pop from empty list")
# except IndexError as e:
#     print(f"An error occurred: {e}")
#     exit()

# popped_element = ls[-1]
# ls = ls[:-1]

# print("The popped element: ", popped_element)
# print("The final list: ", ls)
