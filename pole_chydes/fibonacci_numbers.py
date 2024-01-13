def Fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_gen = Fibonacci_generator()

for _ in range(10):
    print(next(fibonacci_gen))




