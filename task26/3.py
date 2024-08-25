def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
