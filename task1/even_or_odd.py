'''number = int(input('Write the number: '))
if number % 2 == 0:
    print('The number is odd')
else:
    print('The number is even')'''
    
def even_or_odd(number):
    if number % 2 == 0:
        return 'Number is even'
    else:
        return 'Number is odd'
        
number = int(input('Write the number: '))
print(even_or_odd(number))
