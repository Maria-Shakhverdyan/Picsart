def num_sum(n):
    number = str(n)
    num_sum = 0

    for char in number:
        num_sum += int(char)
    print(num_sum)


n = int(input("Enter the number: "))
num_sum(n)