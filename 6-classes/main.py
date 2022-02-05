import data as d
import os
from classes import library


my_library = library.Library("Nathan's Library")
# my_library.set_address()
# my_library.print_address()

my_library.import_books_from_csv()

my_library.list_books()
