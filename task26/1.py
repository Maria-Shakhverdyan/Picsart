def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = 10
fib = fibonacci_generator(n)
print(list(fib))

# 0 1 1 2 3 5 8 13 21 34 ...

# 1. a = 0, b = 1
# 2. a = 1, b = 1
# 3. a = 1, b = 2
# 4. a = 2, b = 3
# 5. a = 3, b = 5 ...