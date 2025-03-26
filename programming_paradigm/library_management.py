class Book:
    """A class representing a book with a title, author, and availability status."""
    
    def __init__(self, title, author):
        """Initialize a Book with title, author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned and available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"

class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty list to store books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out {book}")
                    return
                else:
                    print(f"{book} is already checked out.")
                    return
        print(f"Book with title '{title}' not found.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned {book}")
                    return
                else:
                    print(f"{book} was not checked out.")
                    return
        print(f"Book with title '{title}' not found.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are available at the moment.")
