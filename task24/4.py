
def compose(f, g):
    return lambda x: f(g(x))

def add_2(x):
    return x + 2

def mul_by_4(x):
    return x * 4

composed_func = compose(mul_by_4, add_2)
result = composed_func(5)

print(result)