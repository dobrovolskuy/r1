class Book:
    def __init__(self,title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    @staticmethod

    def books_published_in_year(book_list, target_year):
        count = 0
        for book in book_list:
            if book.year == target_year:
                count += 1
        return count

book_list = [
    Book("Book1", "Author1", 2022, 200),
    Book("Book2", "Author2", 2020, 150),
    Book("Book3", "Author3", 2023, 180),
]

target_year = 2023
result = Book.books_published_in_year(book_list, target_year)
print(f"Number of books published in {target_year} year : {result}")

