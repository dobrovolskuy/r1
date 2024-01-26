def even_odd_generator(i):
    return ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "") or i

for i in range(1, 16)
    result = even_odd_generator(i)
    print(result)
    
results = [even_odd_generator(i) for i in range(1, 16)]
print(results)
