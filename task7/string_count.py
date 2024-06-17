count = int(input("Enter the count of elements: "))
ls = []
string_count = {}

for i in range(count):
    string = input("Enter the string: ")
    ls.append(string)
    
for string in ls:
    if string in string_count:
        string_count[string] += 1
    else:
        string_count[string] = 1

for string in string_count:
    print(f"{string} stringy handipum e {string_count[string]} angam")