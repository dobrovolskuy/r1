def even_odd_generator(i):
    return ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "") or i
result = even_odd_generator(15)
print(result)