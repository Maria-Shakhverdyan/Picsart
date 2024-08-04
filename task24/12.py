def make_memoize(f):
    cache = {}

    def memoize(*args):
        if args in cache:
            return cache[args]
        else:
            result = f(*args)
            cache[args] = result
            return cache[args]
        
    return memoize

def func(x):
    return x * x

memoized_func = make_memoize(func)

print(memoized_func(4))
print(memoized_func(4))
print(memoized_func(5))
