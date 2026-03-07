
import logging
import json
from book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    force=True
)

logging.info("TEST LOG")

class Library:

    def __init__(self):
        logging.info("Library system started")
        self.books = []
        self.load_books()

    def load_books(self):

        try:

            with open("books.json", "r") as f:

                data = json.load(f)

                for b in data:

                    book = Book(b["title"], b["author"])
                    book.available = b["available"]

                    self.books.append(book)

        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save_books(self):

        data = []

        for book in self.books:

            data.append({
                "title": book.title,
                "author": book.author,
                "available": book.available
            })

        with open("books.json", "w") as f:

            json.dump(data, f, indent=4)

    def add_books(self, book):

        self.books.append(book)
        self.save_books()
        logging.info(f"book added: {book.title}")
        print("Book Added")

    def borrow(self, title):

        for book in self.books:

            if book.title == title and book.available:

                book.available = False
                self.save_books()
                logging.info(f"Book borrowed: {book.title}")
                print("Borrowed") 
                return

        print("Not Available")

    def show_books(self):

        if not self.books:

            print("No books available")
            return

        for book in self.books:

            status = "Available" if book.available else "Borrowed"

            print(book.title, "-", book.author, "-", status)

    def return_book(self, title):

        for book in self.books:

            if book.title == title:

                book.available = True
                self.save_books()
                logging.info(f"Book returned: {book.title}")
                print("Book Returned")
                return

        print("Book not found")