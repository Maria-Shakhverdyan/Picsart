def get_nth_element(iterable, n):
    '''
    Returns the n-th element from the iterable using iter() and next().

    Args:
        iterable (iterable): The iterable from which to get the n-th element.
        n (int): The index of the element to retrieve (0-based index).

    Returns:
        The n-th element from the iterable if it exists.
        Raises IndexError if n is out of bounds of the iterable.
    
    Example:
        numbers = [10, 20, 30, 40, 50]
        element = get_nth_element(numbers, 2)
        print(element)  # Output: 30
    '''
    
    iterator = iter(iterable)

    for _ in range(n):
        try:
            next(iterator)
        except StopIteration:
            raise IndexError("Index out of bounds")

    return next(iterator)

numbers = [10, 20, 30, 40, 50]

try:
    element = get_nth_element(numbers, 2)
    print(f"The 3-rd element is: {element}")
except IndexError as e:
    print(e)
