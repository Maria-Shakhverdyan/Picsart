def natural(n):
    if n < 2:
        return 1
    return n + natural(n - 1)

number = int(input("Enter the number: "))
result = natural(number)
print(result)