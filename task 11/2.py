string = "capitalize"

new = ord(string[:1]) - 32
new_string = chr(new) + string[1:]

print(new_string)