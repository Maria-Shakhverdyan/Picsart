string = "banana"
new_string = ""

for char in string:
    if char == 'a':
        new_string += 'x'
    else:
        new_string += char

print(new_string)