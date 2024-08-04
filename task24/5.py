power_factory = lambda x: lambda n: x ** n

print(power_factory(2)(5)) # 32
print(power_factory(4)(5)) # 1024