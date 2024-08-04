mul = lambda factor: lambda x: x * factor

factor = int(input("Enter the factor: "))
mul_by_factor = mul(factor)

x = int(input("Enter the x: "))
result = mul_by_factor(x)

print(result)