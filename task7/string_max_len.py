count = int(input("Enter the count of strings in list: "))
ls = []

for i in range(count):
    string = input(f"Enter string {i + 1}: ")
    ls.append(string)

max_len = ls[0]
max_index = 0

for i in range(1, len(ls)):
    if len(ls[i]) > len(max_len):
        max_len = ls[i]
        max_index = i

print(f"The longest string in the list is '{max_len}' at index '{max_index}'")
