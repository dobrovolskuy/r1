from contextlib import contextmanager
import time

@contextmanager

def Timer():
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time :  {elapsed_time} seconds")


with Timer():
    for _ in range (1000):
        pass