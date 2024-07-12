def find_first_upper(string):
    for char in string:
        if char >= 'A' and char <= 'Z':
            print(char)
            break

string = str(input("Enter the string: "))
find_first_upper(string)