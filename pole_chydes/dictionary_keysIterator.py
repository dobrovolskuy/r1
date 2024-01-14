class DictionaryKeysIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            result = self.keys[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_iterator = DictionaryKeysIterator(my_dict)

for key in keys_iterator:
    print(key)