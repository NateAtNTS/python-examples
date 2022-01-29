############################
# Title: Control Structures
# Description: Demonstrating Control Structures in Python
#
# Date: January 28, 2022
# Author: Nathan A. Bate
#

# Import reusable data
import data as d

# show the books array / list in the data module
# print(data.books)

# let's iterate through the book list and output each book name
i = 1
for book in d.books:
    print(str(i) + ". " + book)
    i = i + 1

# show iterating through a range
print("\nShowing interating through a range")
my_range = list(range(1, 6))
for value in my_range:
    print(value)

# show iterating through a range by two
print("\nShowing iterating through a range by two")
my_range_by_two = list(range(2, 11, 2))
for value in my_range_by_two:
    print(value)

# show off some other numerical functions
print("\nMin in my_range")
print(min(my_range))

print("\nMax in my_range_by_two")
print(max(my_range_by_two))

print("\nsum both lists then add them")
print(sum(my_range) + sum(my_range_by_two))

# showing off pythons comprehension
print("\nshow off python's comprehension compact code")
squares = [value**2 for value in range(1, 21)]
print(squares)

# loop over a tuple
print("\nLooping over the tuple")
for t in d.my_tuple:
    print(t)
