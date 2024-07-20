def calculate(ls):
    if not ls:
        return []
    return ls[0] + calculate(ls[1:])

result = calculate([1, 2, 3])
print(result)