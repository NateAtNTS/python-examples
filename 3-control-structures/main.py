############################
# Title: Control Structures
# Description: Demonstrating Control Structures in Python
#
# Date: January 28, 2022
# Author: Nathan A. Bate
#

# Import reusable data
import data

# show the books array / list in the data module
# print(data.books)

# let's iterate through the book list and output each book name
i = 1
for book in data.books:
    print(str(i) + ". " + book)
    i = i + 1

print("\nShowing interating through a range")

# show iterating through a range
for value in range(1, 11):
    print(value)