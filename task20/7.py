def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

number = int(input("Enter a number: "))
print(is_power_of_two(number))
