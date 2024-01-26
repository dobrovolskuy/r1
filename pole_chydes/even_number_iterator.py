class EvenIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop or self.start % 2 != 0:
            raise StopIteration

        else:
            even_number = self.start
            self.start += 2
            return even_number


start_value = 1
end_value = 10
even_iter = EvenIterator(start_value, end_value)

for even_number in even_iter:
    print(even_number)


