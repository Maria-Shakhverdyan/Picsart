def custom_reduce(func, iterable, initializer=None):
    it = iter(iterable)

    if initializer is None:
        try:
            res = next(it)
        except StopIteration:
            raise ("Empty sequence")
    else:
        res = initializer
    
    for item in it:
        res = func(res, item)
        yield res


add = lambda a, b: a + b
numbers = [num for num in range(1, 20)]

print("Without initializer: ")
for result in custom_reduce(add, numbers):
    print(result)

print("With initializing (0): ")
for result in custom_reduce(add, numbers, 0):
    print(result)