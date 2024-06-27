string = "hello, world! are you ready?"
new_string = ""

new = ord(string[:1]) - 32

for i, char in enumerate(string):
    if i == 0 or string[i - 1] == ' ':
        if 'a' <= char <= 'z':
            new_string += chr(ord(char) - 32)
        else:
            char
    else:
        new_string += char
        
print(new_string)