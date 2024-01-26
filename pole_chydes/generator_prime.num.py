def is_prime(num):
    """Function to check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
         if num % i == 0:
             return False
    return True

def prime_generator():
    """Generator for prime numbers."""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

generator = prime_generator()
for _ in range(10):
    print(next(generator))



