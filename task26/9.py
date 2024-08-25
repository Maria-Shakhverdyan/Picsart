def gen1():
    for num in range(1, 6):
        yield num

def gen2():
    yield from gen1()

    for num in range(6, 11):
        yield num

for value in gen2():
    print(value)