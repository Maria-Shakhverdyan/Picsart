def make_counter():
    counter = 0
    def increment():
        nonlocal counter;
        counter += 1
        return counter
    return increment

counter1 = make_counter()
print("Counter 1 is: ", counter1()) # 1
print("Counter 1 is: ", counter1()) # 2
print("Counter 1 is: ", counter1()) # 3

counter2 = make_counter()
print("Counter 2 is: ", counter2()) # 1
print("Counter 2 is: ", counter2()) # 2

print("Counter 1 is: ", counter1()) # 4