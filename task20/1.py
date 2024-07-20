def flatten_list(nested_list):
    flattened = []
    for element in nested_list:
        if type(element) == list:
            flattened += flatten_list(element)
        else:
            flattened.append(element) 
    return flattened

nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
flattened = flatten_list(nested_list)
print(flattened)