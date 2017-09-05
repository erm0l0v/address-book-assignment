from address_book.book import Book
from address_book.repository import Repository


def create_book():
    book_obj = Book()
    repository_obj = Repository(book_obj)
    return repository_obj
