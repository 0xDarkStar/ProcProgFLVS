# Matthew Rojas
# 14/8/2023
# This program is useless!
# This is meant to ask for the user's name and greet them.
# It then tells them a fact about computational thinking then says goodbye.

import re

'''
Pseudocode:

START OF PROGRAM
    Ask for name
    Greet user using their name
    Provide fact about computational thinking or "great" programming idea
    Say bye to the user (using their name)
END OF PROGRAM
'''

def main():
    # Ask for name
    name = input("What's your name? ")
    # Greet user using their name
    print(f"It's nice to meet you, {name}.", end= "")
    if re.search("[0-9]", name): # There is a number in their name
        print(" That is an interesting name. I haven't seen a name with a number in it before.")
    else: # There isn't a number in their name
        print("")
    # Provide a fact about computational thinking
    print("Computational thinking can help with coming up with the structure for scripts or help with finding solutions to problems.")
    # Say bye to the user (using their name)
    print("Well, that's all I have to say....")
    print(f"I hope you have a good day, {name}!")

main() # Run the code

# Hello Torres! Nice to meet you again.