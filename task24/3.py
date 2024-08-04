def apply_twice(f, x):
    return f(f(x))

def square(n):
    return n * n

result = apply_twice(square, 5)
print("The result of square is: ", result)

def sum(a):
    return a + a

num = int(input("Enter value of a: "))
result = apply_twice(sum, num)
print(result)