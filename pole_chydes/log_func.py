def log_func(func):
    def wrapper(*args, ** kwargs):
        print(f"Function call {func.__name__} with arguments{args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function{func.__name__} completed execution. Result : {result}")
        return result
    return wrapper

@log_func
def add_numbers(a, b):
    return a + b

resul = add_numbers(3, 5)