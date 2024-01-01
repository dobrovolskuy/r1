import time

def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Try again...")
                    attempts += 1
                    time.sleep(1)

            print(f"Maximum number of attempts reached ({max_attempts}). Give up.")
        return wrapper
    return decorator

@retry(max_attempts=3)
def example_function():
    import random
    if random.random() < 0.5:
        raise ValueError("Accidental error")
    else:
        print("Function succeeded!")

example_function()