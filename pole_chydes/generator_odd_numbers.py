def filter_odd_numbers(seguence):
    for number in seguence:
        if number % 2 == 0:
            yield number

numbers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_numbers = filter_odd_numbers(numbers)

for number in filter_numbers:
    print(number)



