def custom_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    min_length = min(len(it) for it in iterables)
    
    for _ in range(min_length):
        yield tuple(next(iterator) for iterator in iterators)


ls1 = [1, 2, 3, 4]
ls2 = ['a', 'b', 'g']
ls3 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

print("The custom_zip result is: ")
for item in custom_zip(ls1, ls2, ls3):
    print(item)