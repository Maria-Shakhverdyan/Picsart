def make_accumulator(start=0):
    total = start
    def accumlator(arg):
        nonlocal total;
        total += arg
        return total
    return accumlator

res = make_accumulator()
print(res(5)) #5
print(res(5)) #10
print(res(10)) #20