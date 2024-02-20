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
import csv

def main():
    try:
        appMode()
    except: # Something happened, at least there's a backup mode!
        print("Error. Switching to terminal mode.")
        termMode()

def termMode():
    print("Hello world")

def appMode():
    global controlFrame, outputFrame, mainWindow
    # Initialize the window
    mainWindow = Tk()
    mainWindow.geometry("700x600")
    # Holds control and output frames
    mainFrame = Frame(mainWindow)
    mainFrame.pack()
    # Holds the controls (Buttons and text inputs)
    controlFrame = Frame(mainFrame)
    controlFrame.pack(side=LEFT, padx=20)
    popFrames.popControlFrame()
    # Holds the output (responses such as "Deleted user" and requested info)
    outputFrame = Frame(mainFrame)
    outputFrame.pack(side=RIGHT, padx=20)
    # Binds ctrl+q to closing the window
    mainWindow.bind('<Control-q>', lambda e: kill(e))
    mainWindow.mainloop()

class popFrames():
    def popControlFrame():
        # Populate the control frame with buttons and text inputs
        removeUser = Button(controlFrame, text="Remove User", padx=10, pady=10, command=commands.delUser)
        addUser = Button(controlFrame, text="Add User", padx=10, pady=10, command=commands.addUser)
        outputList = Button(controlFrame, text="View User List", padx=10, pady=10, command=commands.outList)
        outputUser = Button(controlFrame, text= "View User Info", padx=10,pady=10, command=commands.outUser)
        # Load them all
        removeUser.grid(row=0, column=0)
        addUser.grid(row=0, column=1)
        outputList.grid(row=1, column=0)
        outputUser.grid(row=1, column=1)

    def popOutputFrame():
        print("Populating output frame")
        userList = Listbox(outputFrame)
        userInfo = Listbox(outputFrame)
    
class commands():
    def delUser():
        print()
    def addUser():
        print()
    def outList():
        userInfoCommands.searchUserList()
    def outUser():
        print()

class userInfoCommands():
    def searchUserList():
        with open("battle_royale.csv") as file:
            table = csv.reader(file, delimiter=',')
            rows = [] # To store all the rows for later use
            for row in table:
                index = 0
                for i in row:
                    if index == 2: # Is at the end of the list
                        i = i[2:-2] # To remove the ']
                    else:
                        i = i[2:-1] # To remove the '
                    row[index] = i.lower() # Make it lowercase to have it work with the code
                    index += 1
                rows += [row]
        print(rows)

def kill(e):
    mainWindow.destroy()

main()