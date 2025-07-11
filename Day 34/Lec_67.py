class MyLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)

    def show_book_names(self):
        for book in self.books:
            print(book)

a = MyLibrary()
a.add_book("Book1")
a.add_book("Book2")
a.add_book("Book3")
a.show_book_names()
