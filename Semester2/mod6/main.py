from tkinter import *

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
    Make the questionnaire, but don't pack the frame.
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
    # print(f"Questions: {len(questionsKeys)}, Selected Answer: {answer}, Current Page: {page}, Current Run: {currentRun}")
    if page == len(questionKeys):
        page = 0
        switch_to("back", "questionnaire")
        change_question(page, questionKeys, questionText, pageIndicator)
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
    Make the courses page to show which courses are recommended based on the questionnaire.
    """
    global coursesFrame, mainText
    coursesFrame = Frame(master=mainFrame)
    mainText = Label(master=coursesFrame, text="You have not completed the questionnaire yet.")
    backButton = Button(master=coursesFrame, text="Go Back", command=lambda: switch_to("back", "courses"))
    mainText.pack()
    backButton.pack()

def switch_to(string, location=False):
    """
    Used to switch between menus (from the main menu to others and back)
    """
    match string:
        case "questionnaire":
            mainMenuFrame.forget()
            questionFrame.pack()
        case "research":
            mainMenuFrame.forget()
            researchFrame.pack()
        case "courses":
            mainMenuFrame.forget()
            if len(answers) != 0 and len(answers[0]) == len(questions):
                mainText.configure(text="All attempts of the questionnaire:")
            coursesFrame.pack()
        case "back":
            frames = {"questionnaire": questionFrame,
                    "research": researchFrame,
                    "courses": coursesFrame}
            frames[location].forget()
            removed = 0
            index = 0
            for i in answers:
                if len(i) == 0:
                    answers.pop(index)
                    removed += 1
                index += 1
            mainMenuFrame.pack()

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
                          ["Doctor", "Nurse"],
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