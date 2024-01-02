def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):

        key = (args, frozenset(kwargs.items()))

        if key in cache:
            print("Fetching from cache!")
            return cache[key]

        result = func(*args, **kwargs)

        cache[key] = result
        return result

    return wrapper

@memoize
def add_numbers(a, b):
    print("Calling the add_numbers function")
    return a + b

result1 = add_numbers(3, 5)
print("Result 1:", result1)

result2 = add_numbers(3, 5)
print("Result 2:", result2)

result3 = add_numbers(2, 4)
print("Result 3:", result3)

