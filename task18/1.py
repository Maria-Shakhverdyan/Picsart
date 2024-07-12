def countdown(n):
    if n < 0:
        print("The number must be natural.")
    else:
        print(n)
        if n > 0:
            countdown(n - 1)

n = int(input("Enter the number: "))
countdown(n)
