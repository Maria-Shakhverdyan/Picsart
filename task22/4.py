def manual_iteration(numbers) -> None:
    """
    Manually iterates over a list of numbers using iter() and next().

    Args:
        numbers (list): A list of numbers to iterate over.

    Returns:
        None
    """
    iterator = iter(numbers)

    while True:
        try:
            number = next(iterator)
            print(f"Current number: {number}")
        except StopIteration:
            print("Iteration is complete.")
            break

numbers = [1, 3, 5, 7, 9, 11]
manual_iteration(numbers)
