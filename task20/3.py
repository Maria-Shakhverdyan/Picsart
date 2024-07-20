def is_sorted(ls):
    if not ls or len(ls) == 1:
        return True
    if ls[0] <= ls[1]:
        return is_sorted(ls[1:])
    else:
        return False

result1 = is_sorted([1, 19, 5])
print(result1)
result2 = is_sorted([])
print(result2)
result3 = is_sorted([1, 2, 3, 4, 5])
print(result3)