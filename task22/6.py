def apply_function(iterable, func):
    '''
    Applies a function to each element of the iterable and returns a list of the results.

    Args:
        iterable (iterable): An iterable (e.g., list, tuple) of elements to which the function will be applied.
        func (function): A function to apply to each element of the iterable.

    Returns:
        list: A list of results obtained by applying the function to each element of the iterable.

    Example:
        numbers = [1, 2, 3, 4, 5]
        squared_numbers = apply_function(numbers, lambda x: x ** 2)
        print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
    '''

    results = [func(item) for item in iterable]
    
    return results

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_function(numbers, lambda x: x ** 2)
print(f"Squared numbers: {squared_numbers}")
