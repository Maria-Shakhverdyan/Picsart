def to_lower(s):
    return s.lower()
def to_upper(s):
    return s.upper()
def len_of_str(s):
    return len(s)
def reverse_(s):
    return s[::-1]

str_oper = {
    'lower' : to_lower,
    'upper' : to_upper,
    'len' : len_of_str,
    'reverse' : reverse_
}

def manipulate_string(s, operation):
    if operation not in str_oper:
        raise ValueError("Chka senc operator")
    oper_func = str_oper[operation]

    return oper_func(s)

try:
    print("Lowercase:", manipulate_string("Hello World", 'lower'))   # Outputs: "hello world"
    print("Uppercase:", manipulate_string("Hello World", 'upper'))   # Outputs: "HELLO WORLD"
    print("Length:", manipulate_string("Hello World", 'length'))     # Outputs: 11
    print("Reverse:", manipulate_string("Hello World", 'reverse'))   # Outputs: "dlroW olleH"
except ValueError as e:
    print("Error:", e)