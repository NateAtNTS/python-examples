############################
# Title: User Input
# Description: Demonstrating User input in python
#
# Date: February 3, 2022
# Author: Nathan A. Bate
#
import data


def love_letter():
    print("\nLet's demonstrate some basic user input.")
    print(data.dividing_line)
    your_love_letter = input("Tell me how much you love me: ")
    print("\nHere was your wonderful love letter:")
    print(data.dividing_line)

    # see the following link for some ways to color text
    # https://ozzmaker.com/add-colour-to-text-in-python/
    print("\033[1;32;48m" + your_love_letter)


def age_survey():
    print("\033[0;38;48m\nMake sure to type cast when needed.")
    print(data.dividing_line)
    question = "Yo, how old are you?\nI know that is a personal question! "
    question += "But I don't care! I am going to ask anyway! \nYour age: "
    user_age = input(question)
    try:
        user_age = float(user_age)
    except ValueError as ex:
        print(f"You moron! {user_age} is not an age! This program is quitting now since you don't play fair.")
        return False
    else:
        # I don't want to display a .0 on an integer, so I will type cast it to an int if it isn't a float
        if user_age.is_integer():
            user_age = int(user_age)
        print(f"You are an awesome {user_age} year old!")
    finally:
        print("\nThanks for participating in this wonderful survey.")

    return True


the_love = True
while the_love:

    love_letter()
    if not age_survey():
        break

    print("\nLet's see if you want to continue with the love.")
    print(data.dividing_line)
    quit_check = input("Do you want to continue this program? (y/n): ")
    if quit_check == 'n':
        the_love = False
