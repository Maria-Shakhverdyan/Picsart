def exception_propagator(iterable):
    for value in iterable:
        if value == 'error':
            raise ValueError("An error occurred!")
        else:
            yield value

ls = exception_propagator([1, 2, 3, 'a', 'error', 'Maria', 456])

try:
    for value in ls:
        print(value)
except ValueError as e:
    print(e)