from datetime import datetime, timedelta

def rate_limit(max_calls, period):
    def decorator(func):
        calls = 0
        last_reset_time = datetime.now()

        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset_time


            current_time = datetime.now()
            if current_time - last_reset_time >= timedelta(seconds=period):
                calls = 0
                last_reset_time = current_time


            if calls < max_calls:
                result = func(*args, **kwargs)
                calls += 1
                return result
            else:
                print(f"Call limited. Maximum number of calls ({max_calls}) reached.")
                return None

        return wrapper

    return decorator


@rate_limit(max_calls=2, period=5)
def my_function():
    print("Function called.")

my_function()
my_function()
my_function()
