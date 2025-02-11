from enum import Enum
from typing import Dict, Optional
from pydantic import BaseModel


class Genre(str, Enum):
    """Book genres."""
    SCI_FI = "Science Fiction"
    FANTASY = "Fantasy"
    HORROR = "Horror"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    THRILLER = "Thriller"


class Book(BaseModel):
    """Book schema"""
    id: int
    title: str
    author: str
    publication_year: int
    genre: Genre


class InMemoryDB:
    def __init__(self):
        self.books: Dict[int, Book] = {}

    def get_books(self) -> Dict[int, Book]:
        """Gets books from database."""
        return self.books

    def add_book(self, book: Book) -> Book:
        """Adds book to database."""
        self.books[book.id] = book
        return book

    def get_book(self, book_id: int) -> Optional[Book]:
        """Gets a specific book from database."""
        return self.books.get(book_id)

    def update_book(self, book_id: int, data: Book) -> Optional[Book]:
        """Updates a specific book in database."""
        if book_id not in self.books:
            return None
        self.books[book_id] = data
        return self.books[book_id]

    def delete_book(self, book_id: int) -> bool:
        """Deletes a specific book from database."""
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
