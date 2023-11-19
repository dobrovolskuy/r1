
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None

result = divide_numbers(4, 2)

if result is not None:
    print(f"Result of dividing 4 by 2 is {result}")