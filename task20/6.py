def fib_list(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    fib = [0, 1, 1]
    for _ in range(3, n):
        fib.append(fib[-1] + fib[-2])
    return fib

n = int(input("Enter the number: "))
print(fib_list(n))

#0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12...
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...