def ls_len(lst):
    if not lst:
        return 0
    return 1 + ls_len(lst[1:])

result = ls_len([1, 2, 3, 4, 5])
print(result)