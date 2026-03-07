from book import Book
from library import Library

library = Library()

while True:

    print("\n1 Add Book")
    print("2 Show Books")
    print("3 Borrow Book")
    print("4 Return Book")
    print("5 Exit")

    try:

        ch = input("Enter choice: ")

        if ch == "1":

            title = input("Book title: ")
            author = input("Author: ")

            book = Book(title, author)

            library.add_books(book)

        elif ch == "2":

            library.show_books()

        elif ch == "3":

            title = input("Enter title: ")

            library.borrow(title)

        elif ch == "4":

            title = input("Enter title: ")

            library.return_book(title)

        elif ch == "5":

            print("Goodbye!")
            break

        else:
            print("Invalid choice")

    except Exception as e:

        print("Error occurred:", e)