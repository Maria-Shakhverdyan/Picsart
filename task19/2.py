def print_numbers(n):
    if n <= 0:
        return
    if (n > 0) and (n <= 5):
        print(n)
    print_numbers(n - 1)
    
print_numbers(5)
