def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

temp_oper = {
    ('celsius', 'fahrenheit'): celsius_to_fahrenheit,
    ('celsius', 'kelvin'): celsius_to_kelvin,
    ('fahrenheit', 'celsius'): fahrenheit_to_celsius,
    ('fahrenheit', 'kelvin'): fahrenheit_to_kelvin,
    ('kelvin', 'celsius'): kelvin_to_celsius,
    ('kelvin', 'fahrenheit'): kelvin_to_fahrenheit,
}

def convert_temperature(value, from_unit, to_unit):
    if (from_unit, to_unit) not in temp_oper:
        raise ValueError("Chka senc ban.")
    converter = temp_oper[(from_unit, to_unit)]
    return converter(value)

try:
    print("From Celsius to Kelvin:", convert_temperature(25, 'celsius', 'kelvin'))         # Outputs: 298.15
    print("From Fahrenheit to Celsius:", convert_temperature(77, 'fahrenheit', 'celsius')) # Outputs: 25.0
    print("From Celsius to Fahrenheit:", convert_temperature(25, 'celsius', 'fahrenheit')) # Outputs: 77.0
    print("From Kelvin to Celsius:", convert_temperature(300, 'kelvin', 'celsius'))        # Outputs: 26.85
    print("From Kelvin to Fahrenheit:", convert_temperature(300, 'kelvin', 'fahrenheit'))  # Outputs: 80.33
    print("From Fahrenheit to Kelvin:", convert_temperature(77, 'fahrenheit', 'kelvin'))   # Outputs: 298.15

except ValueError as e:
    print("Error:", e)