import time
def timeit(funk):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = funk(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function execution time:{funk.__name__} {elapsed_time}  seconds")
        return result
    return wrapper
@timeit
def add_numbers (a, b):
    return a + b
resul = add_numbers(3, 5)


