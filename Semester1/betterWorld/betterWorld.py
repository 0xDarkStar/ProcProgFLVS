# Matthew Rojas
# 8/14/2023
# This script is meant to inform the user on how they can help make the world a better place.

from time import sleep
import os

'''
Ways the user can try to help make the world a better place:
 - Don't use disposable items
 - Lower your carbon footprint (and don't support companies that have high carbon emissions)
 - Walk, bicycle, or use public transit more to get to where you want to go
 - Make your city more human-centric
'''

denied = ["no", "n", "nope", "nah", "nuh-uh", "nuh uh"]

def main():
    name = input("Hello, user. Before I continue, may I ask for a name to refer to you by. ") # Ask for their name
    if name.lower() in denied or len(name) == 0: # They didn't give us a name
        print("Okay, Then I'll continue to refer to you as \"user\".")
        name = "user" # Their name is "user". Doesn't really matter though
    else: # They chose a name
        print(f"Okay, I'll refer to use as {name} from now on.") # Call them by that name
    sleep(.5)
    print(f"Nice to meet you, " + name + ". Now that we're acquainted, let's talk about something that matters to all of us: making the world a better place. We all share a desire to create a positive impact in our communities and beyond.") # Thank you ChatGPT, I was really stuck here.
    sleep(2) # This is the last time we call them by their name.
    print("There are multiple issues with our current world. Some of the issues that we have can't be fixed alone, we need to stick together to make a change.")
    sleep(1) # Tell them the problems with our world
    print("""The issues are:
          A) Climate Change
          B) Evironmental Pollution""")
    input("Which of these problems would you like to learn more about? ") # Ask them a meaningless question
    sleep(2)
    print("It doesn't matter what you put there. :)", end= "\r") # Tell them that it was meaningless
    sleep(.5)
    if "torres" in name.lower():
        print("I was planning on doing more, but I can't find something like getch in the normal functions of Python. :/ \nI'll try to finish it then possibly use it in a later assignment. It will use keyboard since that's the only thing I can think of.")
        sleep(4)
    while True == True: # Loop to show solutions
        os.system("clear")
        print("""There are multiple solutions to the problems. Those solutions being:
            A) Don't use disposable items
            B) Lowering your carbon footprint (and not supporting companies that have high carbon emissions)
            C) Using other modes of transportation to get around
            D) Making your city more human-centric""") # Tell them the solutions
        choice = input("Which of these solutions would you like to learn more about? ").lower() # Ask them what solution do they want to see
        match choice[0]:
            case "a": # They want to know about disposable items
                print("You can help with pollution by not using disposable items as much. This means not buying disposable cups, disposable utensils, disposable plates, pretty much anything with \"disposable\" in the name")
                stop = input("Do you want to see the other solutions? (y/n) ").lower() # Ask if they want to look at the other solutions
                if stop[0] == "n": # They don't
                    print("Well, I hope you learned something.")
                    exit() # End the program
            case "b": # They want to know about lowering their carbon footprint
                print("""You can help with climate change by lowering you carbon footprint, which means: 
 - not using your car as much if at all
 - Using less power
 - Using renewable energy to power your stuff""")
                print("You can also not support companies that have a high carbon footprint. Sure, one person not buying might not affect them too much if at all, but if a big enough number of people boycott them, the company would want to become more evironmentally friendly to get those customers back.")
                stop = input("Do you want to see the other solutions? (y/n) ").lower() # Ask if they want to look at the other solutions
                if stop[0] == "n": # They don't
                    print("Well, I hope you learned something.")
                    exit() # End the program
            case "c": # They want to know about using other modes of transportation
                print("""You can also help with climate change by using other modes of transportation. These other modes of transportation can be:
 - Walking
 - Cycling
 - Taking the bus
 - Taking a train
 - Carpooling""")
                stop = input("Do you want to see the other solutions? (y/n) ").lower() # Ask if they want to look at the other solutions
                if stop[0] == "n": # They don't
                    print("Well, I hope you learned something.")
                    exit() # End the program
            case "d": # They want to know about making their city more human-centric
                print("Making your city more human-centric will help with climate change as well. When a city becomes more human-centric and less car-centric, people are more likely to walk, cycle, or take the bus to places instead of getting into a metal box alone, driving there, looking for a spot to leave the metal box, then doing whatever they planned on doing.")
                stop = input("Do you want to see the other solutions? (y/n) ").lower() # Ask if they want to look at the other solutions
                if stop[0] == "n": # They don't
                    print("Well, I hope you learned something.")
                    exit() # End the program

main() # Run the entire thing