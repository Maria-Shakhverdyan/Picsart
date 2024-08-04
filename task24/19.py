import math

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculate_mode(data):
    frequency_dict = {}
    for num in data:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    max_count = max(frequency_dict.values())
    mode = [k for k, v in frequency_dict.items() if v == max_count]

    if len(mode) == 1:
        return mode[0]
    else:
        return mode

def calculate_standard_deviation(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

analyze_opers = {
    'mean' : calculate_mean,
    'median' : calculate_median,
    'mode' : calculate_mode,
    'standart_deviation' : calculate_standard_deviation
}

def analyze_data(data, operation):
    if operation not in analyze_opers:
        raise ValueError("Chka senc operacia")
    analyze_func = analyze_opers[operation]
    return analyze_func(data)

ls = [1, 2, 3, 4, 4, 5, 5]
try:
    print("The mean is: ", analyze_data(ls, 'mean'))
    print("The median is: ", analyze_data(ls, 'median'))
    print("The mode is: ", analyze_data(ls, 'mode'))
    print("The standard deviation is: ", analyze_data(ls, 'standart_deviation'))
except ValueError as e:
    print(e)
