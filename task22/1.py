def my_map(func: callable, iterable: list) -> list:
    '''
    Args:
        func (callable): A function that takes a single argument and returns a result.
        iterable (list): A list of elements to be processed by the function.

    Returns:
        list: A list of results after applying the given function to each element in the iterable.

    How it works:
        - The function iterates over each element in the provided iterable.
        - It applies the given function to each element.
        - It collects the results in a list and returns this list.

    Example:
        def square(x):
            return x * x

        numbers = [1, 2, 3, 4]
        squared_numbers = my_map(square, numbers)
        print(squared_numbers)  # Output: [1, 4, 9, 16]
    '''

    result = []

    for item in iterable:
        result.append(func(item))

    return result

def square(x: int) -> int:
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = my_map(square, numbers)

print(squared_numbers)
