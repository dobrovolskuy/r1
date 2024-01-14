class PalindromeIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def is_palindrome(self, word):
        return word == word[::-1]

    def __next__(self):
        while self.index < len(self.words):
            current_word = self.words[self.index]
            self.index += 1
            if self.is_palindrome(current_word):
                return current_word

        raise StopIteration

word_list = ["level", "python", "radar", "racecar", "programming"]
palindrome_iterator = PalindromeIterator(word_list)

for palindrome in palindrome_iterator:
    print(palindrome)