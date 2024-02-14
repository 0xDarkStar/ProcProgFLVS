# Made By: 0xDarkStar
# Purpose: Search a .csv file for sunrise times. Search by month and day or by time, I don't really care.



import csv
from getpass import getpass # Acting as a bandaid for line 177
import re

months = { # Change three letter versions into full name versions
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}
dayTranslate = { # Change all word form days to numbers
    "first":            "1st",
    "second":           "2nd",
    "third":            "3rd",
    "fourth":           "4th",
    "fifth":            "5th",
    "sixth":            "6th",
    "seventh":          "7th",
    "eighth":           "8th",
    "ninth":            "9th",
    "tenth":            "10th",
    "eleventh":         "11th",
    "twelfth":          "12th",
    "thirteenth":       "13th",
    "fourteenth":       "14th",
    "fifteenth":        "15th",
    "sixteenth":        "16th",
    "seventeenth":      "17th",
    "eighteenth":       "18th",
    "nineteenth":       "19th",
    "twentieth":        "20th",
    "twenty-first":     "21st",
    "twenty-second":    "22nd",
    "twenty-third":     "23rd",
    "twenty-fourth":    "24th",
    "twenty-fifth":     "25th",
    "twenty-sixth":     "26th",
    "twenty-seventh":   "27th",
    "twenty-eighth":    "28th",
    "twenty-ninth":     "29th",
    "thirtieth":        "30th",
    "thirty-first":     "31st"
}

def main():
    print("Hello, this bad program is here to help you find the time of sunrises for months January to May and days 1 to 19!\nThis does nothing else but tell you if there is a date with that time or what time the sun rises for that date.")
    userDate = input("Enter your time or date in any format: ")
    date = checkAll(userDate) # Check every part of the string (get the time or date in the string)
    if type(date[0]) != int: # If date doesn't hold the time
        lookInFile(month=date[0], day=date[1])
    else: # If date does hold the time
        lookInFile(time=date)

def checkAll(inputStr):
    """
    Calls all check functions to find the month and date or time asked.
    Then asks if said month and date or time is correct.
    """
    try: # Look for the time
        date = checkTime(inputStr)
        timePresent = 0
    except:
        timePresent = 1
    try: # No time found, look for the day and month
        date = checkMonth(inputStr)
        datePresent = 0
    except:
        datePresent = 1
    if timePresent == 1 and datePresent == 1:
        print("No time or date was input, please make sure you inputed the proper times/dates.")
        exit()
    hold = checkChoice(date) # Double check that the specified date/time is what they want to look for
    return hold

def checkMonth(inputStr):
    """
    Checks the given string to look for a month
    """
    # Search pattern to look for months
    pattern = r"(?=\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)|(((\d{2})|(\d))[-/]((\d{2})|(\d))))"
    # First part looks for words beginning in the specified three letters (Could catch words such as "Janitor", too lazy to fix)
    # Second part looks for numbers that look like ##/## or #/## or ##/# or #/#


    # Find all matches
    matches = re.findall(pattern, inputStr, flags=re.IGNORECASE)
    # Handle results
    if matches:
        if len(matches[0][0]) > 0:
            # Grabs the three letter version of the month
            month = matches[0][0].lower()
            day = checkDay(inputStr)
        else:
            # Grabs the number version of the date, splitting it into month and day
            try:
                month, day = matches[0][1].split("/") # Date looks like ##/##
            except ValueError:
                month, day = matches[0][1].split("-") # Date looks like ##-##
            if int(month) <= 0 or int(day) <= 0: # Either month or day is too low of a value
                print("The month or day number you entered is too low, please check your values.")
                userDate = input("Enter your date in any format: ") # Ask again
                month, day = checkMonth(userDate) # Check it once more
                return [month, day]
            try: # Grabs the three letter version of the month
                month = list(months.keys())[int(month)-1]
                day = list(dayTranslate.keys())[int(day)-1]
                day = dayTranslate[day]
            except IndexError: # It went out of range, possibly because of the date being DD-MM or DD/MM instead of MM-DD or MM/DD
                try: # Flip it and try splitting ##/##
                    day, month = matches[0][1].split("/")
                except ValueError: # Flip it and split ##-##
                    day, month = matches[0][1].split("-")
                try: # Try to grab the three letter version of the month again
                    month = list(months.keys())[int(month)-1]
                    day = list(dayTranslate.keys())[int(day)-1]
                    day = dayTranslate[day]
                except IndexError: # Since both numbers were too high, ask them to input the date again
                    print("The month or day number you entered is too high, please check your values.")
                    userDate = input("Enter your date in any format: ") # Ask again
                    month, day = checkMonth(userDate) # Check again
        return [month, day]
    else: # Nothing was found, script will end.
        exit()

def checkDay(inputStr):
    """
    Finds a day in the given string.
    """
    pattern = r"(?=\b(?:(\d{1,2}(?:(st|nd|rd|th)?))|(first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|twenty-first|twenty-second|twenty-third|twenty-fourth|twenty-fifth|twenty-sixth|twenty-seventh|twenty-eighth|twenty-ninth|thirtieth|thirty-first))\b)"

    matches = re.findall(pattern, inputStr, flags=re.IGNORECASE)
    # Matches would look like [('15th', 'th', 'fifteenth')]
    if matches[0][0]:
        day = matches[0][0]
        if len(day) <= 2:
            if int(day) >= 31:
                day = "31st"
            else:
                day = list(dayTranslate.keys())[int(day)-1]
                day = dayTranslate[day]
        else:
            if int(day[:-2]) >= 31:
                day = "31st"
        return day
    else:
        day = matches[0][-1]
        day = dayTranslate[day]
        return day

def checkChoice(date):
    """
    Checks if they really wanted that month and day or time
    """
    if len(date) == 2:
        yesNo = input(f"Do you want to check for a time for \"{months[date[0]]}, {date[1]}\"? [Y/n] ").lower()
        if yesNo[0] == "n":
            userDate = input("Enter your time or date in any format: ")
            date = checkAll(userDate)
            return date
        elif yesNo[0] == "y" or len(yesNo) == 0:
            return date
    else:
        print("\x1b[2mYou won't be able to see your input here because of some weird error using input()...\x1b[22m")
        yesNo = getpass(f"Do you want to check for a date with a sunrise at \"{date[0]}\"? [Y/n] ").lower() # Weird error here if I use input instead of getpass. IDK why
        if yesNo[0] == "n": # Change the time/date
            userDate = input("Enter your time or date in any format: ")
            date = checkAll(userDate)
            return date
        elif yesNo[0] == "y" or len(yesNo) == 0:
            return [int(date[0][:-3]), date[0][-2:]]

def checkTime(inputStr):
    """
    Finds the time in the given string
    """
    pattern = r"(?=\b((([0-2]\d)|(\d))[:]([0-5]\d)))"

    matches = re.findall(pattern, inputStr, flags=re.IGNORECASE)
    hours = matches[0][1]
    minutes = matches[0][-1]
    if int(hours) > 24:
        print("That is not how a 24 hour time works. Proper times are between 00:00 and 24:00")
    elif int(hours) == 24 and int(minutes) > 0:
        print("That is not how a 24 hour time works. Proper times are between 00:00 and 24:00")
    else:
        print(f"{hours}:{minutes}")
        return [f"{hours}:{minutes}"]

# Search the CSV file for times that are asked.

def lookInFile(month=None, day=None, time=None):
    with open("sun_data.csv") as file:
        table = csv.reader(file, delimiter=',')
        rows = [] # To store all the rows for later use
        for row in table:
            index = 0
            for i in row:
                if index == 5: # Is at the end of the list
                    i = i[2:-2] # To remove the ']
                else:
                    i = i[2:-1] # To remove the '
                row[index] = i.lower() # Make it lowercase to have it work with the code
                index += 1
            rows += [row]
    if month != None:
        try: # Try to grab the index of the month
            monthInd = rows[0].index(month)
        except ValueError: # Month was not found
            print("The requested month is not in our database.")
            exit()
        else:
            try: # Try to grab the time of sunrise during that day
                time = rows[int(day[:-2])][monthInd]
            except IndexError: # Day was not found
                print("The requested day is not in our database.")
                exit()
            else:
                month = months[month]
                print(f"A time was found!\nThe sunrise for {month} the {day} is {time[0]}:{time[1:]}")
    else:
        try:
            timeCheck = f"{time[0]}{time[1]}"
            day = 0
            for i in rows:
                if timeCheck in i:
                    month = i.index(timeCheck)
                    break
                day += 1
            month = list(months.keys())[int(month)-1]
            day = list(dayTranslate.keys())[int(day)-1]
            day = dayTranslate[day]
            print(f"A time was found!\nThe sun rises at {time[0]}:{time[1]} on {months[month]} the {day}.")
        except TypeError:
            print("No date was found with a sunrise at that time.")

main()

input_strings = ["What is the sunrise for the 1st of January?",
                "Can you tell me the sunrise for January 2nd?",
                "I'm curious about the sunrise on 3/15",
                "What's the sunrise for March 15th?",
                "Do you know the sunrise time for 04-20?",
                "Sunrise for April 20th, please."]