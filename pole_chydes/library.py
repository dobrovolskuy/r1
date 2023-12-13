class Library:
    def __init__(self,):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        if not self.books:
            return "The library is empty."
        else:
            book_list = "\n".join(str(book) for book in self.books)
            return f"library books:\n {book_list}"


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

library = Library()

book1 = Book(title="Kobzar" , author="Taras Shevchenko ", year=1840)
book2 = Book(title="Invocation", author="Lesya Ukrainka", year=1907)
book3 = Book(title="The Museum of Abandoned Secrets", author="GOksana Zabuzhko", year=2009)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library)



