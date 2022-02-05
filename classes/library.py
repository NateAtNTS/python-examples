from classes import address
from classes import books


class Library:
    """Basic Properties and Methods Pertaining to a library"""

    def __init__(self, library_name):
        """Initialize the Library"""
        self.name = library_name
        self.address = address.Address
        self.books = books.Books

    def set_address(self):
        """Set the address of the library using an address object"""
        self.address.set_address(self.address)

    def print_address(self):
        self.address.display(self.address)

    def import_books_from_csv(self):
        self.books.load_from_csv(self.books)

    def list_books(self):
        self.books.list_books(self.books)
