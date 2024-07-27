def process_data(data, /, *, operation = 'sum'):
    try:
        if not isinstance(data, list):
            raise TypeError("Data is not list.")
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Elements is not numbers.")
        
        if operation == 'sum':
            return sum(data)
        if operation == 'min':
            return min(data)
        if operation == 'max':
            return max(data)
        if operation == 'average':
            return sum(data) / len(data) if data else 0
        else:
            raise ValueError("Unsupported operation.")
    except TypeError as te:
        print(f"TypeError as: {te}")
        return None
    except ValueError as ve:
        print(f"ValueError as: {ve}")
        return None

data = [1, 5, 8, 4, 5, 44, 453]
result = process_data(data, operation = 'sum')
print("The sum is: ", result)

result = process_data(data, operation = 'max')
print("The max value in list is: ", result)

result = process_data(data, operation = 'min')
print("The min value in list is: ", result)

result = process_data(data, operation = 'average')
print("The average is: ", result)