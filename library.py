from book import Book

class Library:
    def __init__(self):
        self.books=[]
    def add_books(self,book):
        self.books.append(book)
        print("Book Added")
    def borrow(self,title):
        for i in self.books:
            if i.title==title and i.available==True:
                i.available=False
                print("Brrowed")
                return
        print("Not Available")

    def show_books(self):

        if not self.books:
            print("No books available")
            return

        for book in self.books:

            status = "Available" if book.available else "Borrowed"

            print(book.title, "-", book.auth, "-", status)
    
    def return_book(self,title):
        for i in self.books:
            if i.title==title:
                i.available=True
                print("book retured")
                return
        print("book not found")

