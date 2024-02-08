

import re

months = {
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

def main():
    userDate = input("Enter your date in any format: ")
    checkAll(userDate)

def checkAll(inputStr):
    """
    Calls all check functions to find the month and date asked.
    Then asks if said month and date is correct.
    """
    month, day = checkMonth(inputStr)
    hold = checkChoice(month, day)
    
    if type(hold) == list:
        month = hold[0]
        day = hold[1]
    return month, day

def checkMonth(inputStr):
    """
    Checks the given string to look for a month
    """
    # Search pattern to look for months
    pattern = r"(?=\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)|(((\d{2})|(\d))[-/]((\d\d)|(\d))))"
    # First part looks for words beginning in the specified three letters (Could catch words such as "Janitor", too lazy to fix)
    # Second part looks for numbers that look like 00/00 or 0/00 or 00/0 or 0/0


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
            month, day = matches[0][1].split("/")
            if int(month) <= 0 or int(day) <= 0:
                print("The month or day number you entered is too low, please check your values.")
                userDate = input("Enter your date in any format: ")
                month, day = checkMonth(userDate)
                return month, day
            # Grabs the three letter version of the month
            try:
                month = list(months.keys())[int(month)-1]
            except IndexError:
                day = matches[0][1].split("/")[0]
                month = matches[0][1].split("/")[1]
                print(f"month: {month}, day: {day}")
                try:
                    month = list(months.keys())[int(month)-1]
                except IndexError:
                    print("The month or day number you entered is too high, please check your values.")
                    userDate = input("Enter your date in any format: ")
                    month, day = checkMonth(userDate)
        return month, day
    else:
        print("No valid month keyword found.")
        return 0

def checkDay(inputStr):
    """
    Finds a day in the given string.
    """
    pattern = r"(?=\b(((([0-3]\d)|([1-9]))(st|nd|rd|th|\b|.))|(first|second|third|fourth|fifth|sixth|seventh|eighth|nineth|tenth|eleventh|twelveth|)))"

    matches = re.findall(pattern, inputStr, flags=re.IGNORECASE)
    if matches[2][2]:
        return matches[2][2]
    else:
        return matches[2][0]

def checkChoice(month, day):
    """
    Checks if they really wanted that month and day
    """
    yesNo = input(f"Do you want to check for a time for \"{months[month]}, {day}\"? [Y/n] ").lower()
    if yesNo[0] == "n":
        print("What date do you want?")
    elif yesNo[0] == "y" or len(yesNo) == 0:
        return 0


main()

input_strings = ["What is the sunrise for the 1st of January?",
                "Can you tell me the sunrise for January 2nd?",
                "I'm curious about the sunrise on 3/15",
                "What's the sunrise for March 15th?",
                "Do you know the sunrise time for 04-20?",
                "Sunrise for April 20th, please."]