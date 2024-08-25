def repeat_element(element, times):
    count = 0
    while count < times:
        yield element
        count += 1

example1 = repeat_element('barev', 5)
for index, i in enumerate(example1):
    print("First example: ", index + 1, i)

example2 = repeat_element('vonc es?', 10)
for index, i in enumerate(example2):
    print("Second example: ", index + 1, i)