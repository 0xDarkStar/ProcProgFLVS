# Made by: 0xDarkStar
# Creation Date: 8/28/2023
# Short description:
# This file hold functions which, when used by other files, would create a menu that is navigable using arrow keys.

import keyboard # To read the inputs
import os # To clear the screen
from time import sleep # To give them time to let go of keys
class Menu:
    def __init__(self, options: list, title=False, description=False):
        self.options = options # The options for the menu
        self.title = title # The title for the menu (If the have one)
        self.description = description
        self.endex = (len(options)-1) # The index of the final option
        self.index = 0 # The starting index

    def startMenu(self):
        while True == True:
            os.system("clear") # Clear the terminal
            if self.title != False: # If they have a title
                print(f"\x1B[1;28m {self.title}\n\x1B[22m") # Print it in bold
            if self.description != False: # If they have a description
                print(f"{self.description}\n") # Print the description
            count = 0
            for i in self.options: # Print out their options
                if i == self.options[self.index]: # If this is the selected option...
                    if count == 0:
                        print(f"\x1B[28m\x1B[?25l    \x1B[30;47m{i}\x1B[0;0m") # Swap the colors (highlight)
                    else:
                        if i == "Back":
                            print(f"\x1B[28m\x1B[?25l    \x1B[30;47m{i}\x1B[0;0m") # Swap the colors (highlight)
                        else:
                            oldCount = 0 + count
                            count = 0
                            while True:
                                if i[-1] != " ":
                                    break
                                elif i[count] != " " and i[count + 1] == " ":
                                    i = i[:count+1]
                                    break
                                elif i[count] != " " and i[count + 2] == " ":
                                    i = i[:count+1]
                                    break
                                else:
                                    count -= 1
                            print(f"\x1B[28m\x1B[?25l    \x1B[30;47m{i}\x1B[0;0m") # Swap the colors (highlight)
                            count = oldCount
                else: # If it isn't...
                    print("\x1B[28m   ", i) # Print it normally
                count += 1
            print("\n\x1B[2m  Use the arrow keys and spacebar to navigate the menu\x1B[22m") # Tell them how to use the menu
            print("\x1B[8m", end="\r") # Hide their inputs
            arrow = keyboard.read_key() # Read their input
            match arrow: # Find out what the input is
                case "up": # Their input was the up arrow
                    if self.index == 0: # Their selected option is the first one (top)
                        self.index = self.endex # Change their selected option to the final one (bottom)
                    else: # Their selected option isn't the top
                        self.index -= 1 # Move them up by one
                case "down": # Their input was the down arrow
                    if self.index == self.endex: # Their selected options is the final one (bottom)
                        self.index = 0 # Change their selected to the top
                    else: # Their selected option isn't the bottom
                        self.index += 1 # Move it down by one
                case "space": # Their input was the spacebar
                    choice = self.options[self.index] # They chose this one
                    print("\x1B[?25h\x1B[28m") # Reset everything
                    sleep(.2)
                    return choice # Return their choice for processing
                case "esc": # Their input was the escape button
                    print("\x1B[?25h\x1B[28m") # Reset everything
                    break # Break the menu
            sleep(.1) # Give them time to let go of the key they pressed
