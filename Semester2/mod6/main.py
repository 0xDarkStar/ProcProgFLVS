from tkinter import *
from datetime import datetime
import time

"""Remaining parts to be compelted:
[ ] Algorithm for recommending courses
[ ] Courses page
[ ] Research page
[ ] All the questions and answers
[ ] All the courses and their descriptions.
Possible additions: 
[ ] Save questionnaire answers between instances
[ ] Make the UI look better
"""

def main():
    global mainFrame # Allow mainFrame to be accessed from anywhere
    mainWindow = Tk()
    mainWindow.title("Recommend Major")
    mainFrame = Frame(master=mainWindow, padx=20, pady=20)
    # Make all the menus
    main_menu()
    questionnaire()
    research()
    courses()
    mainFrame.pack() # Show the mainFrame
    mainWindow.mainloop() # Start the program

def main_menu():
    """
    Make the main menu
    """
    global mainMenuFrame
    mainMenuFrame = Frame(master=mainFrame)
    menuButton0 = Button(master=mainMenuFrame, text="Take questionnaire", command=lambda:switch_to("questionnaire"))
    menuButton1 = Button(master=mainMenuFrame, text="Show research for this project", command=lambda: switch_to("research"))
    menuButton2 = Button(master=mainMenuFrame, text="Show course matchups", command=lambda: switch_to("courses"))
    menuButton0.pack()
    menuButton1.pack()
    menuButton2.pack()
    mainMenuFrame.pack()

def questionnaire():
    """
    Make the questionnaire, but don't pack the frame
    """
    global questionFrame, answers, page, questions
    questions = {"I work with others on projects": "Teamwork",
                 "I like working outdoors": "Work Outdoors",
                 "I like working indoors": "Work Indoors"}
    answers = [] # Holds all the answers that the user chose
    page = 0
    questionKeys = list(questions.keys())
    currentQuestion = questionKeys[page]
    questionFrame = Frame(master=mainFrame)
    pageIndicator = Label(master=questionFrame, text=f"{page+1}/{len(questionKeys)}")
    questionText = Label(master=questionFrame, text=currentQuestion)
    answerFrame = Frame(master=questionFrame)
    answerButton0 = Button(master=answerFrame, text="Never", command=lambda: answer_clicked(1, questionKeys, questionText, pageIndicator))
    answerButton1 = Button(master=answerFrame, text="Rarely", command=lambda: answer_clicked(2, questionKeys, questionText, pageIndicator))
    answerButton2 = Button(master=answerFrame, text="Occasionally", command=lambda: answer_clicked(3, questionKeys, questionText, pageIndicator))
    answerButton3 = Button(master=answerFrame, text="Often", command=lambda: answer_clicked(4, questionKeys, questionText, pageIndicator))
    answerButton4 = Button(master=answerFrame, text="Very Often", command=lambda: answer_clicked(5, questionKeys, questionText, pageIndicator))
    backButton = Button(master=questionFrame, text="Go Back", command=lambda: switch_to("back", "questionnaire"))
    pageIndicator.pack()
    questionText.pack()
    answerButton0.pack(side=LEFT)
    answerButton1.pack(side=LEFT)
    answerButton2.pack(side=LEFT)
    answerButton3.pack(side=LEFT)
    answerButton4.pack(side=LEFT)
    answerFrame.pack()
    backButton.pack()

def answer_clicked(answer, questionKeys, questionText, pageIndicator):
    """
    Handle changing the page and adding the chosen answer to the list
    """
    global page
    if page == 0:
        answers.append([])
    currentRun = len(answers)-1
    answers[currentRun].append(answer)
    page += 1
    if page == len(questionKeys):
        page = 0
        switch_to("back", "questionnaire")
        change_question(page, questionKeys, questionText, pageIndicator)
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        answers[currentRun].append(date)
    else:
        change_question(page, questionKeys, questionText, pageIndicator)

def change_question(page, questionKeys, questionText, pageIndicator):
    """
    Handle updating the question, page indicator, and all the answers
    """
    currentQuestion = questionKeys[page]
    pageIndicator.configure(text=f"{page+1}/{len(questionKeys)}")
    questionText.configure(text=currentQuestion)

def research():
    """
    Make the research page
    """
    global researchFrame
    researchFrame = Frame(master=mainFrame)

def courses():
    """
    Make the courses page to show which courses are recommended based on the questionnaire
    """
    global coursesFrame, mainText, attemptIndex, attemptsList
    coursesFrame = Frame(master=mainFrame)
    mainText = Label(master=coursesFrame, text="You have not completed the questionnaire yet.")
    attemptsFrame = Frame(master=coursesFrame)
    listScroll = Scrollbar(master=attemptsFrame)
    attemptsList = Listbox(master=attemptsFrame, width=30, yscrollcommand=listScroll.set)
    listScroll.config(command=attemptsList.yview)
    attemptsControlFrame = Frame(master=attemptsFrame, height=10)
    selectAttemptButton = Button(master=attemptsControlFrame, text="View Selected Attempt", command=lambda: switch_to("attempt", attemptIndex=attemptsList.curselection()))
    backButton = Button(master=coursesFrame, text="Go Back", command=lambda: switch_to("back", "courses"))
    mainText.pack()
    attemptsFrame.pack()
    attemptsList.pack(side=LEFT)
    listScroll.pack(side=LEFT, fill=Y)
    attemptsControlFrame.pack(side=LEFT)
    selectAttemptButton.pack()
    backButton.pack()
    attempt() # Make the attempt page

def attempt():
    """
    Make the attempt page as to show that attempt's answers for each question and the recommended courses
    """
    global attemptFrame, attemptText, attemptQADict, topMajorsParts
    attemptQADict = {}
    attemptFrame = Frame(master=mainFrame)
    attemptText = Label(master=attemptFrame, text=f"Attempt number: Filler\nDate taken: Filler")
    # Frame for Questions and answers as well as all the labels
    QAFrame = Frame(master=attemptFrame)
    for i in range(len(questions)):
        attemptQADict[i] = [Label(master=QAFrame, text=list(questions.keys())[i], relief="sunken", width=30, height=2), Label(master=QAFrame, text="Answer", relief="sunken", width=15, height=2)]
        attemptQADict[i][0].grid(column=0, row=i)
        attemptQADict[i][1].grid(column=1, row=i)
    # Frame for the recommended majors (top 3)
    majorsFrame = Frame(master=attemptFrame, padx=5)
    major0 = {"match":5, "canvas":5, "name":5, "desc":5}
    major1 = {"match":5, "canvas":5, "name":5, "desc":5}
    major2 = {"match":5, "canvas":5, "name":5, "desc":5}
    topMajorsParts = [major0, major1, major2]
    make_majors_parts(major0, majorsFrame)
    make_majors_parts(major1, majorsFrame)
    make_majors_parts(major2, majorsFrame)
    # Back button then packing
    backButton = Button(master=attemptFrame, text="Go Back", command=lambda: switch_to("back", "attempt"))
    attemptText.pack()
    QAFrame.pack(side=LEFT)
    backButton.pack(side=BOTTOM)
    majorsFrame.pack(side=RIGHT)

def make_majors_parts(majorDict, majorFrame):
    majorDict["match"] = Label(master=majorFrame, text="##% match")
    majorDict["match"].pack()
    majorDict["canvas"] = Canvas(master=majorFrame, height=5, width=100, background="black")
    majorDict["canvas"].pack()
    majorDict["name"] = Label(master=majorFrame, text="Recommended major", font="TkHeadingFont")
    majorDict["name"].pack()
    majorDict["desc"] = Label(master=majorFrame, text="Major Description")
    majorDict["desc"].pack()

def switch_to(destination, currentLocation=False, attemptIndex=0):
    """
    Used to switch between menus (from the main menu to others and back)
    """
    match destination:
        case "questionnaire":
            mainMenuFrame.forget()
            questionFrame.pack()
        case "research":
            mainMenuFrame.forget()
            researchFrame.pack()
        case "courses":
            mainMenuFrame.forget()
            if len(answers) != 0 and len(answers[0]) == (len(questions)+1): # If there is at least one completed attempt
                mainText.configure(text="All attempts of the questionnaire:") # Change the text
                attemptIndex = 1 # Update the attempts List
                attemptsList.delete(0,END)
                for i in answers:
                    attemptString = f"Attempt {attemptIndex}, {i[-1]}"
                    attemptsList.insert(attemptIndex, attemptString)
                    attemptIndex += 1
            else:
                mainText.configure(text="You have not completed the questionnaire yet.")
            coursesFrame.pack()
        case "attempt":
            if len(attemptIndex) > 0:
                mainText.configure(text="All attempts of the questionnaire:")
                coursesFrame.forget()
                attemptText.configure(text=f"Attempt number: {attemptIndex[0]+1}\nDate taken: {answers[attemptIndex[0]][-1]}")
                # Update all answers in the QAFrame to be accurate
                index = 0
                answerConvert = ["Never", "Rarely", "Occasionally", "Often", "Very Often"]
                for i in list(questions.keys()):
                    currentAnswer = answers[attemptIndex[0]-1][index]
                    attemptQADict[index][0].configure(text=i)
                    attemptQADict[index][1].configure(text=answerConvert[currentAnswer-1])
                    index += 1
                topMajorsParts[0]["canvas"].create_rectangle(0, 0, 50, 5, fill="green") # Percentage match bar (replace 50 with the percentage)
                topMajorsParts[0]["match"].configure(text="50% match") # Percentage match text (replace the 50 with the percentage)
                attemptFrame.pack()
            else:
                mainText.configure(text="No attempt was selected.")
        case "back":
            frames = {"questionnaire": questionFrame,
                    "research": researchFrame,
                    "courses": coursesFrame,
                    "attempt": attemptFrame}
            frames[currentLocation].forget() # Forget the correct frame
            # Clean the answers array of any empty attempts
            removed = 0
            index = 0
            for i in answers:
                if len(i) == 0:
                    answers.pop(index)
                    removed += 1
                index += 1
            if currentLocation == "attempt":
                # Clear all the bars
                topMajorsParts[0]["canvas"].delete("all")
                topMajorsParts[1]["canvas"].delete("all")
                topMajorsParts[2]["canvas"].delete("all")
                coursesFrame.pack()
            else:
                mainMenuFrame.pack()

def change_shown_majors(attemptIndex):
    """
    Changes the labels and canvases for each major.
    """

def recommend_courses():
    """
    The majors in the dictionary will work like this:
    majors = {"Template": ["Description", ["List", "Of", "Career", "Paths"], ["Working with others", "Working Outdoors", "Working Indoors", etc.]],
            "Example": ["Often does X, Y, and Z. Has to ... often.", ["Job1", "Job2", "Job3", "Job4"], [5, 3, 3, ...]]}
    """
    majors = {"Geology": ["Description",
                          ["Geologist"],
                          []],
              "Biology": ["Description",
                          ["Biologist"],
                          []],
              "Psychology": ["Description",
                             ["Psychologist"],
                             []],
              "Computer Science": ["Description",
                                   [""],
                                   []],
              "Computer Programming": ["Description",
                                       ["Back-end Developer", "Front-end Developer"],
                                       []],
              "Engineering": ["Description",
                              ["Automotive Engineer"],
                              []],
              "Education": ["Description",
                            ["Teacher"],
                            []],
              "Buisness": ["Description",
                           ["Manager"],
                           []],
              "Finance": ["Description",
                          ["Accountant"],
                          []],
              "Medical": ["Description",
                          ["Doctor", "Nurse", "Surgeon"],
                          []],
              "History": ["Description",
                          ["Historian"],
                          []],
              "Law": ["Description",
                      ["Lawyer"],
                      []]}
    """
    The algorithm for recommending courses (as far as I've planned), will recommend based on the difference between set points and chosen answers.

    That can be done by checking an answer, using the index of the answer to find out what skill it is related to, then going through all the majors' to subtract against that one skill, adding each result to a list.
    Said list will have an integer in it for each major. That integer is what is added to by each result (according to the major). Before adding a result though, make sure that the result is positive (make it absolute).

    It could recommend the top three courses or only the course(s) that match the most.
    """

main()
