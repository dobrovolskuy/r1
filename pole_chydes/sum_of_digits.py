def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10)

number = 12345
print("Sum of digits", number, "Eguals", sum_of_digits(number))