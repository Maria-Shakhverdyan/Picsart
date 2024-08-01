def make_multiplier_of():
    n = int(input("Enter the number: "))
    
    def multiplier(k):
        return n * k
    
    return multiplier

mul_function = make_multiplier_of()

print(mul_function(5)) # n * 5
print(mul_function(10)) # n * 10


# def make_multiplier_of(n):    
#     def multiplier(k):
#         return n * k
    
#     return multiplier

# mul_of_5 = make_multiplier_of(5)
# mul_of_7 = make_multiplier_of(7)
# mul_of_10 = make_multiplier_of(10)

# print(mul_of_5(7))   # Output: 35
# print(mul_of_7(4))   # Output: 28
# print(mul_of_10(8))   # Output: 80