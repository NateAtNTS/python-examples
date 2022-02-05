
import data as d
import os


class Books:
    """Loading, printing, and managing a collection of books"""

    books = {}
    book_properties = []
    list_length = int(os.getenv("ITEMS_PER_PAGE"))

    def load_from_csv(self):
        """Attempt to load a list of books from the specified CSV"""
        print("Attempting to load books from CSV")
        print(d.dividing_line)
        csv_load_result = d.load_csv("nathansBooks.csv")
        self.book_properties = csv_load_result['columns']
        self.books = csv_load_result['rows']
        print(d.dividing_line)
        # print(self.books)


    def list_books(self):
        items_index = 1
        running_total = 1
        for book in self.books:
            while items_index <= self.list_length:
                print(f"{running_total}. {self.books[running_total]['title']}")
                running_total += 1
                items_index += 1

            response = input("Press enter to continue or q+enter to quit the list: ")
            if response == "q":
                break
            else:
                items_index = 1


