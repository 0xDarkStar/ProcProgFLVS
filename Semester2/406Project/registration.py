# By: 0xDarkStar
# Purpose: Make a UI that would allow users to control who is/isn't registered.
# Examples:
# 1. Removing a person from the list
# 2. Adding a person to the list
# 3. Looking at the entire list
# 4. Looking at all the info of a specified person.

''' What to use:
1. tkinter (for the UI)
2. idk
'''
from tkinter import *

def main():
    try:
        appMode()
    except:
        print("Unknown Error. Switching to terminal mode.")
        termMode()

def termMode():
    print("Hello world")

def appMode():
    mainWindow = Tk()
    mainWindow.geometry("700x600")
    mainFrame = Frame(mainWindow)
    mainFrame.pack()
    leftFrame = Frame(mainFrame)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(mainFrame)
    rightFrame.pack(side=RIGHT)
    explanationText = Label(mainFrame, text="I'm gay")
    explanationText.pack(side=TOP)
    mainWindow.mainloop()

main()