"""
This module defines a library management system with classes for book
and library, showcasing how a library works in OOP
"""

class Book:
    """
    This class implements the logic to create a new book
    """
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self._is_checked_out = False

    def return_book(self):
        return f"The book '{self.title}' by '{self.author}' has been created")

class Library:
    """
    This class simulates how a library works and implements methods to add a book,
    check_out a book (borrow) and return a borrowed book
    """
    def __init__(self):
        self._books = []

    def add_book(self, book) -> None:
        """
        This method adds a book to the library and marks the book
        as available for checkout
        """
        self._books.append(book)

    def check_out_book(self, title: str) -> None:
        """
        This method changes the state of the book is_checked_out to false
        indicating that the book isn't available for borrowing
        """
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    return
                book._is_checked_out = True
                return

    def return_book(self, title: str) -> None:
        """
        This method changes the state of the book's is_checked_out to true
        indicating the book has been returned and is avaialbe for borrowing
        """
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    return
                book._is_checked_out = False
                return

    def list_available_books(self) -> None:
        available = [book for book in self._books if not book._is_checked_out]
        if not available:
            print("No books available right now.")
        else:
            for book in available:
                print(f"{book.title} by {book.author}")
