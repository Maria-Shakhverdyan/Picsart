def make_adder(n):
    def adder(x):
        return x + n
    return adder

n = int(input("Enter N value: "))
x = int(input("Enter X value: "))

print(make_adder(n)(x))