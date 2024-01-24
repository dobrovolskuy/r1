def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

N = 5
result_seguence = list(square_generator(N))
print(result_seguence)



