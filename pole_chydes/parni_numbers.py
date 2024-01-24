class ParniIterator:
    def __init__(self, start, end):
        self.curent = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.curent > self.end:
            raise StopIteration
        else:
            current_value = self.curent
            self.curent += 2
            return current_value


start_value = 20
end_value = 40
parni_iter = ParniIterator(start_value, end_value)

for parne_number in parni_iter:
    print(parne_number)

