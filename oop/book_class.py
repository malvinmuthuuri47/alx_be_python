"""
This module defines a class and implements specific magic methods to enhance
its functionality.
"""
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        A function that returns a string representation of the instance
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        A function that returns an official representation of the instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self) -> None:
        """
        A function that's called when the object is deleted or no longer
        referenced by the program
        """
        print(f"Deleting {self.title}")
