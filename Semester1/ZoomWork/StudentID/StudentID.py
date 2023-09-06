# Matthew Rojas
# 17/8/2023
# Make a student ID card

import re
import random
from datetime import date
from tkinter import *
from tkinter import ttk

# Assign a grade to the student. Base off of DOB
grades = {
    6: "1st Grade",
    7: "2nd Grade",
    8: "3rd Grade",
    9: "4th Grade",
    10: "5th Grade",
    11: "6th Grade",
    12: "7th Grade",
    13: "8th Grade",
    14: "9th Grade",
    15: "10th Grade",
    16: "11th Grade",
    17: "12th Grade",
    18: "12th Grade",
}

def findAge(userDOB: list, dateNow: list):
    age = dateNow[0] - userDOB[0]
    if dateNow[1] < userDOB[1]:
        age = age - 1
    elif dateNow[1] == userDOB[1] and dateNow[2] < userDOB[2]:
        age = age - 1
    return age

def showID(userNameF, userNameL, idNumber, userDOB, userGrade, tk):
    print("Hi :)")

def main():
    # Generate ID number
    idNumber = str(random.randint(0, 999999))
    idString = "000000"
    for x in range(len(idNumber)):
        idString = idString[1:]
    idString += idNumber
    # Ask for User's name
    userNameF = input("What is your first name? ")
    userNameL = input("What is your last name? ")
    # Ask for User's DOB
    userDOB = str(input("What is your Date Of Birth? Write it like Year-Month-Day (2009-12-17). ")).lower()
    # Make it easier to use
    userDOBL = [int(userDOB[:4]), int(userDOB[5:7]), int(userDOB[8:10])]
    print(userDOBL)
    # Get today's date
    dateNow = str(date.today())
    # Make it easier to use
    dateNowL = [int(dateNow[:4]), int(dateNow[5:7]), int(dateNow[8:])]
    print(dateNow)
    print(dateNowL)
    age = findAge(userDOBL, dateNowL)
    print(age)
main()