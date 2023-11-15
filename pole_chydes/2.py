def get_two_numbers():
    try:
        num1 = int(input("enter your number:"))
        num2 = int(input("enter your number:"))
        print(f"entered number :{num1} and {num2}")
        return num1, num2
    except ValueError:
        print("you must enter a number!")


get_two_numbers()

