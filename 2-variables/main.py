############################
# Title: Variables
# Description: Demonstrate Variables in Python
#
# Date: January 28, 2022
# Author: Nathan A. Bate
#

string_message = "This is my beautiful python string!"

# demonstrate that I can use a number with a variable name and how to include a quote and escape quotes
string_message_2 = "yo! Here is a quote for you 'Be Cool not hot' or \"this is really cool escaping\""

# you cannot start a variable with a number
# 2_string_message

print("\n***********************************************")
print(string_message)

# this shows how to combine variables
print("\n" + string_message_2)
print("***********************************************\n")

# showing off the title method on a string
my_name = "nate bate"
my_name_upper = "NATE BATE"
print("my name as a title: " + my_name.title())
print("my name as all upper with upper method: " + my_name.upper())
print("my name as all lower with lower method: " + my_name_upper.lower())

# checking out interpolation
first_name = "Nate"
last_name = "Bate"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"\n\nDear {first_name},\n\nWhat do you think about having the last name {last_name}?\n\nSincerely,\n{full_name}")

# demonstrating stripping white space and method chaining....
white_space_example = " both ends have white space "
white_space_example = white_space_example.rstrip().lstrip()

# this does the same thing as above
# white_space_example = white_space_example.strip()

print(white_space_example)

# show integers
my_age = 10
my_wifes_age = 20.5
print("\n\nShowing numbers")
print(my_age + my_wifes_age)

# a lot of decimals
print("\n\nRounding a number: ")
big_decimal = 1.2230002030304005050404040
print(big_decimal.__round__(3))

# multiple assignment
one, two, three = 1,2,3
print("\nThe result of multiple assignment")
print(one + two + three)

# python doesn't have constants, but historically programmers have put constants in all caps.
MY_CONSTANT = "This should never be changed"
print("\nMy Constant")
print(MY_CONSTANT)

import this

# lets do a list...I"m used to calling these arrays
books = ['LOTR', 'Foundation', 'WingFeather Saga', "Chronicles of Narnia"]
original_book_list = books.copy()

print("\nMy book list")
print(books)

# in programming you start counting at 0 in many langauges. So that is why the third element in this list has an index of 2
print("\nAccess the third element in the list")
print(books[2])

# change the value of one of the elements
books[3] = "The " + books[3]

# here is an alternate way to access an array element
print(f"My children really liked \"{books[len(books)-1]}\" when I read it to them a few years ago.")

# add a book to the list
books.append("The Green Ember Series")
print("\nThe book list now that I have added something to it")
print(books)

# insert a new element at a certain index
books.insert(0, "The Mysterious Benedict Society")
print("\nShow the book list with a new first element")
print(books)

# remove an element from the array. in this case I am removing "LOTR"
del(books[1])
print("\nThe book list with element two deleted")
print(books)

# the new element at index 1 now that I have deleted "LOTR" is "Foundation"
print(books[1])

# lets pop the last element on the book stack
popped_book = books.pop()
print("\npopped book")
print(popped_book)

print("\nbooks after pop")
print(books)

second_popped_book = books.pop(0)
print("\nLet's look at my second popped book but this time with an index")
print(second_popped_book)

print("\nBooks after second pop at index")
print(books)

# now let's remove an array element by its value
print("\nRemove by value result")
books.remove("Foundation")
print(books)

# now let's sort!
print("\nOriginal Book list is")
print(original_book_list)

print("\nNow let's sort it temporarily")
print(sorted(original_book_list))

print("\nNow let's sort it temporarily in reverse")
print(sorted(original_book_list, reverse=True))

print("\nNotice now the the list is back in its original order")
print(original_book_list)

print("\nNow let's reverse the list")
original_book_list.reverse()
print(original_book_list)

print("\nNow let's sort it permanently")
original_book_list.sort()
print(original_book_list)
print("\nReverse Sort")
original_book_list.sort(reverse=True)
print(original_book_list)

# another way to access the last element in the list
print("\nAnother way to access the last element in the list")
print(original_book_list[-1])

# now time for a tuple - a list that cannot change
print("\nShowing off a tuple")
my_tuple = (10, 20, 30, 40)
print(my_tuple)
print(my_tuple[1])
