def is_prime(number):
    if number <= 1:
        print("Not prime.")
    elif number <= 3:
        print("Prime.")

    for i in range(2, int(number ** 0.5) + 1):
        if (number % i) == 0:
            return ("Not prime")
        else:
            return ("Prime")

    
number = int(input("Enter the number: "))
print(is_prime(number))