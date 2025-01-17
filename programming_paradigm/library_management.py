# library_management.py

class Book:
    def __init__(self, title, author):
        """Initializes a Book with title, author, and a default status of not checked out."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Book is initially available

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # The book is already checked out

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # The book is already available

    def is_available(self):
        """Returns whether the book is available for checkout."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initializes an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title if it's available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {title}")
                    return
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                    return
        print(f"Sorry, '{title}' is not in the library.")

    def return_book(self, title):
        """Returns a book by title to the library."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {title}")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Sorry, '{title}' is not in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
