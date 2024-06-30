ls = []
n = int(input("Enter the list: "))
count = 0

while count < n:
    element = (int(input("Enter the element: ")))
    ls.append(element)
    count += 1
    
delete = int(input("Enter the number to delete: "))

if delete not in ls:
    print("The number is not exist.")
else:
    ls = [i for i in ls if i != delete]
# else:
#     new = []
#     for i in ls:
#         if i != delete:
#             new.append(i)
        
print("The final list: ", ls)