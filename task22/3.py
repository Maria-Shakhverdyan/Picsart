def my_zip(*iterables) -> list:
    '''
    Args:
        *iterables: Multiple iterable arguments (e.g., lists, tuples). Each iterable should have the same or different lengths.

    Returns:
        A list of tuples, where each tuple contains one element from each of the iterables.
        The function stops zipping when the shortest iterable is exhausted.

    How it works:
        - The function finds the length of the shortest iterable.
        - It iterates through each iterable up to the length of the shortest one.
        - It collects elements at the same index from each iterable into a tuple.
        - It appends each tuple to a result list and returns this list.

    Example:
        numbers = [1, 2, 3]
        letters = ['a', 'b', 'c']
        results = my_zip(numbers, letters)
        print(results)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

    Example with different lengths:
        numbers = [1, 2, 3, 4]
        letters = ['a', 'b']
        results = my_zip(numbers, letters)
        print(results)  # Output: [(1, 'a'), (2, 'b')]
    '''

    min_length = min(len(iterable) for iterable in iterables)

    result = []

    for i in range(min_length):
        tuple_elements = tuple(iterable[i] for iterable in iterables)
        result.append(tuple_elements)

    return result

numbers = [1, 2, 3, 4]
letters = ['Maria', 'John', 'Bob']

zipped_results = my_zip(numbers, letters)

print(zipped_results)
