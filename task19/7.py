def reverse_string(str):
    if str == "":
        return str
    else:
        return reverse_string(str[1:]) + str[0]

result = reverse_string("hello")
print(result)