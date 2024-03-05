# By: 0xDarkStar
# Purpose: Make a UI that would allow users to control who is/isn't registered.
# Examples:
# 1. Removing a person from the list
# 2. Adding a person to the list

''' What to use:
1. tkinter (for the UI)
2. idk
'''
from tkinter import *
from tkinter import messagebox # Good for checking if user is sure about choice
from tkinter import ttk
import csv

def main():
    try:
        app_mode()
    except: # Something happened, at least there's a backup mode!
        print("Error. Switching to terminal mode.")
        terminal_mode()

def terminal_mode(): # Finish this last
    print("Hello world")

def app_mode():
    global controlFrame, outputFrame, mainWindow
    # Initialize the window
    mainWindow = Tk()
    mainWindow.title("Applicant Manipulation")
    mainWindow.geometry("700x300")
    # Holds control and output frames
    mainFrame = Frame(mainWindow)
    mainFrame.pack()
    # Holds the controls (Buttons and text inputs)
    controlFrame = Frame(mainFrame)
    controlFrame.grid(row=0, column=0, padx=20, pady=5)
    pop_frames.pop_control_frame()
    # Holds the output (like the list of users), also contains a search frame for viewing specific users
    outputFrame = Frame(mainFrame)
    outputFrame.grid(row=0, column=1, padx=20, pady=5)
    pop_frames.pop_output_frame()
    # Binds ctrl+q to closing the window
    mainWindow.bind('<Control-q>', lambda e: kill(e))
    mainWindow.mainloop()

def kill(e = False):
    mainWindow.destroy()

class pop_frames():
    def pop_control_frame():
        """
        Populate the 'control' frame, which holds almost all of the controls
        """
        # print("Populating control frame")
        global userNameInput, realNameInput
        # Populate the control frame with buttons and text inputs
        removeUser = Button(controlFrame, text="Remove User", padx=10, pady=10, command=commands.del_user)
        addUser = Button(controlFrame, text="Add User", padx=10, pady=10, command=commands.add_user)
        userNameInput = Entry(controlFrame, width=15)
        realNameInput = Entry(controlFrame, width=10)
        # Load them all
        removeUser.grid(row=0, column=0)
        addUser.grid(row=0, column=1)
        userNameInput.grid(row=1, column=0)
        userNameInput.insert(0, 'Username')
        realNameInput.grid(row=1, column=1)
        realNameInput.insert(0, 'Real name')

    def pop_output_frame():
        """
        Populate the 'output' frame, which holds the output (user list).
        It also makes the search frame and its items meant for searching the user list.
        """
        # print("Populating output frame")
        global userList, searchInput
        # Make the search bar frame
        searchFrame = Frame(outputFrame)
        searchFrame.pack(side=TOP)
        # Make the search bar
        searchBut = Button(searchFrame, text="Search", padx=10, pady=10, command=commands.search_users)
        searchInput = Entry(searchFrame, width=15)
        resetBut = Button(searchFrame, text="Reset", padx=10, pady=10, command=file_commands.update_user_list)
        # Pack the search bar
        searchInput.pack(side=LEFT)
        searchInput.insert(0, "Search")
        searchInput.bind('<Return>', commands.search_users)
        searchBut.pack(padx=5, side=LEFT)
        resetBut.pack(side=LEFT)
        # Make the table that holds all of the user info
        userList = ttk.Treeview(outputFrame)
        # Make the top columns for userList
        userList["columns"] = ("username", "realName", "userID")
        userList.column("#0", width=0, stretch=NO)
        userList.column("username", anchor=CENTER, width=120)
        userList.column("realName", anchor=CENTER, width=100)
        userList.column("userID", anchor=CENTER, width=80)
        userList.heading("#0", text="", anchor=CENTER)
        userList.heading("username", text="Username", anchor=CENTER)
        userList.heading("realName", text="Real Name", anchor=CENTER)
        userList.heading("userID", text="User ID", anchor=CENTER)
        # Load userList
        userList.pack(padx=10, pady=10, side=BOTTOM)
        file_commands.update_user_list()
    
class commands():
    def del_user():
        # Grab the selected item ID from the table
        userID = userList.focus()
        if len(userNameInput.get()) != 0:
            username = userNameInput.get().lower()
            users = file_commands.read_file()
            users.pop(0)
            index = 0
            for i in users:
                if username == i[0].lower():
                    userID = i[2]
                    break
                index += 1
        elif len(realNameInput.get()) != 0:
            realname = realNameInput.get().lower()
            users = file_commands.read_file()
            users.pop(0)
            index = 0
            for i in users:
                if realname == i[1].lower():
                    userID = i[2]
                    break
                index += 1
        try:
            user = userList.item(int(userID))
        except ValueError:
            print("User not found. Are the text inputs empty?")
            return
        username = user["values"][0]
        if not messagebox.askyesno(title="Deletion Check", message=f"Are you sure you want to delete user \n{username} (ID: {userID})?"):
            # They don't want to delete the selected user
            return
        userList.delete(userID)
        file_commands.delete_user(userID)
    def add_user():
        userName = userNameInput.get()
        realName = realNameInput.get()
        file_commands.add_user(userName, realName)
    def search_users(e = False):
        searchTerm = searchInput.get().lower()
        if len(searchTerm) == 0:
            file_commands.update_user_list()
        else:
            users = file_commands.read_file()
            users.pop(0)
            index = 0
            foundUsers = []
            for i in users:
                for ii in i:
                    if searchTerm == ii.lower():
                        foundUsers.append(index)
                index += 1
            for i in userList.get_children(): # All This and down is like update_user_list, just using a different list
                userList.delete(i)
            for i in foundUsers:
                valList = []
                for ii in users[i]:
                    valList.append(ii)
                userList.insert(parent='', index='end', iid=index, values=(valList[0], valList[1], valList[2]))
                index += 1
            userList.update()
        

class file_commands():
    def update_user_list():
        """
        Reads the entire CSV file and displays it on the table userList
        """
        for i in userList.get_children():
            userList.delete(i)
        rows = file_commands.read_file()
        rows.pop(0)
        index = 1
        for i in rows:
            valList = []
            for ii in i:
                valList.append(ii)
            userList.insert(parent='', index='end', iid=index, values=(valList[0], valList[1], valList[2]))
            index += 1
        userList.update()
    def delete_user(iid):
        """
        Uses given index to go into csv file, delete the row, and update all following user IDs.
        """
        rows = file_commands.read_file()
        iid = int(iid)
        rows.pop(iid)
        newRows = []
        for i in rows:
            if i[2] == str(iid+1):
                i[2] = str(iid)
                iid += 1
            newRows += i
        with open("battle_royale.csv", "w") as file:
            for i in rows:
                file.write(f"{i}\n")
        file_commands.update_user_list()
    def add_user(userName, realName):
        """
        Find the length of the user list to find the ID of new user.
        Make new user by adding user info (username, real name, and user ID) to the rows
        write the entire file again, with the new user
        """
        rows = file_commands.read_file()
        userID = str(len(rows))
        rows.append([userName, realName, userID])
        with open("battle_royale.csv", "w") as file:
            for i in rows:
                file.write(f"{i}\n")
        file_commands.update_user_list()
    def read_file():
        """
        Read the file and return all of the lists in the file
        """
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
                    row[index] = i
                    index += 1
                rows += [row]
        return rows


main()