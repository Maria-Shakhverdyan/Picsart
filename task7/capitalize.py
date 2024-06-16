count = int(input("Enter the count of strings in list: "))
ls = []

for i in range(count):
    string = input(f"Enter string {i + 1}: ")
    ls.append(string)
    
for string in range(len(ls)):
    ls[string] = ls[string].capitalize()

print(ls)
