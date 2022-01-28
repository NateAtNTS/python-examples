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
