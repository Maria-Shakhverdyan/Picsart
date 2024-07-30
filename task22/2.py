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
    try:
        if not callable(predicate):
            raise TypeError("func must be callable")
    except TypeError as e:
        print(f"Error: {e}")
        return []
    result = []
    
    try:
        iterator = iter(iterable)
    except TypeError as e:
        print(f"Error: {e}")
        return []
    
    try:
        results = [predicate(item) for item in iterable]
    except Exception as e:
        print(f"Error while applying function: {e}")
        return []

    return results

    for item in iterable:
        if predicate(item):
            result.append(item)

    return result

def is_odd(x: int) -> int:
    return x % 2 != 0

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = my_filter(is_odd, numbers)

print(odd_numbers)
