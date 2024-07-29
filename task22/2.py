def my_filter(predicate: callable, iterable: list) -> list:
    '''
    Args:
        predicate: A function that takes an element and returns True if the element 
                   should be included in the output list, and False otherwise.
        iterable: An iterable (e.g., list, tuple) containing elements to be filtered.

    Returns:
        A list of elements for which the predicate function returns True.

    How it works:
        - The function iterates over each element in the provided iterable.
        - It applies the predicate function to each element.
        - If the predicate returns True for an element, the element is included in the output list.
        - If the predicate returns False, the element is excluded from the output list.
        - Finally, it returns a list containing only the elements that satisfy the predicate function.

    Example:
        def is_odd(x):
            return x % 2 != 0

        numbers = [1, 2, 3, 4, 5, 6]
        odd_numbers = my_filter(is_odd, numbers)

        print(odd_numbers)
    '''
    
    result = []

    for item in iterable:
        if predicate(item):
            result.append(item)

    return result

def is_odd(x: int) -> int:
    return x % 2 != 0

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = my_filter(is_odd, numbers)

print(odd_numbers)
