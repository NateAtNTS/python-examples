############################
# Title: Functions
# Description: Demonstrating Functions in python
#
# Date: February 3, 2022
# Author: Nathan A. Bate
#
import data


def simple_function(high_temp, unit_type):
    """Displays the high temperature for today with the specified unit type"""
    print(f"The high temperature today will be {high_temp} {unit_type}.")


def default_val_check(my_string=""):
    """This showcases what you can do with a default value."""
    if my_string == "":
        return "You did not enter anything!"
    else:
        return f"You entered: {my_string}"


def modify_list(my_list):
    """Demonstrates Modifying a list is a global scope"""
    print("\nLet's show the list before we pop it: ")
    print(data.dividing_line)
    print(my_list)
    my_list.pop()


print("\n\nCall function the positional way")
print(data.dividing_line)
simple_function(70, "degrees")

print("\n\nCall function the keyword way")
print(data.dividing_line)
simple_function(unit_type="celsius", high_temp=20)

print(""
      "Let's show off default values on functions. "
      "There are a lot of times when you want to check if there is a value at all."
      "")
print(data.dividing_line)
print(default_val_check(input("Just press enter without inputting anything: ")))

modify_list(data.books)
print("\nNow we are out of the function, and we are going to print the list again and see.")
print(data.books)

