string = "radar"
new_string = None

for char in string:
    new_string = string[::-1]

if string == new_string:
    print("Yes")
else:
    print("No")



# reverse = "reverse me"
# new_string = ""

# for char in reverse:
#     new_string = char + new_string

# print(new_string)