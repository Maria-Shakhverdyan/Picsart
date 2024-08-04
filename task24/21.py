def sorting(lst):
    return sorted(lst)

def reversing(lst):
    return lst[::-1]

def filtering(lst, condition):
    return [x for x in lst if condition(x)]

def mapping(lst, func):
    return [func(x) for x in lst]

transform_opers = {
    'sort' : sorting,
    'reverse' : reversing,
    'filter' : filtering,
    'map' : mapping
}

list_operations = {
    'sort': sorting,
    'reverse': reversing,
    'filter': filtering,
    'map': mapping
}

def transform_list(lst, operation, *args):
    if operation not in list_operations:
        raise ValueError("Chka senc operacia")

    transform_func = list_operations[operation]

    if operation in ['filter', 'map']:
        if not args:
            raise ValueError(f"{operation} need argument")
        return transform_func(lst, *args)
    else:
        return transform_func(lst)

numbers = [1, 5, 2, 4, 3]

try:
    print("Sorted list:", transform_list(numbers, 'sort'))
    print("Reversed list:", transform_list(numbers, 'reverse'))
    print("Filtered list (if odd):", transform_list(numbers, 'filter', lambda x: x % 2 != 0))
    print("Mapped list (if odd):", transform_list(numbers, 'map', lambda x: x % 2 != 0))
except ValueError as e:
    print(e)
