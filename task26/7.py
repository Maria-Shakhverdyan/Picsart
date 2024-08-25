def custom_range(start, end, step):
    if step <= 0:
        raise ValueError("The step must be greater than 0.")
    while start < end:
        yield start
        start += step

try:
    gen = custom_range(1, 5, 0.5)
    for number in gen:
        print(number)
except Exception as e:
    print(e)

try:
    gen = custom_range(1, 5, 0)
    for number in gen:
        print(number)
except Exception as e:
    print(e)
