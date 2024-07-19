def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

input_string = "amama"
result = is_palindrome(input_string)
print(f"Is '{input_string}' a palindrome? {result}")
