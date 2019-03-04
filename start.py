import clinical
import os
import pygame



def main():
    Player().get_name("player")

    

class Player(object):
    
    def get_name(self, name):
        # LOCAL VARIABLES
        # The player enters their name and gets assigned to a variable called "name"
        name = str
        name = input(">> What's your name? \n> ")
        print(name)

        # This is just an alternative name that the game wants to call the player
        alt_name = "Pink Fluffy Unicorn"
        answer = input(
            ">> Your name is {}, is that correct? [Y|N] \n> ".format(alt_name.upper()))
        if answer.lower() in ["y", "yes"]:
            name = alt_name
            print(">> You are fun, {}! Let's begin our adventure!".format(name.upper()))
        elif answer.lower() in ["n", "no"]:
            print(">> Ok, picky. {} it is. Let's get started on our adventure.".format(
                name.upper()))
        else:
            print(">> Trying to be funny? Well, you will now be called {} anyway.".format(
                alt_name.upper()))
            name = alt_name

        # Now notice that we are returning the variable called name.
        # In main(), it doesn't know what the variable "name" is, as it only exists in
        # get_name() function.
        # This is why indentation is important, variables declared in this block only exists in that block
        return name

if __name__ == "__main__":
    main()

    
