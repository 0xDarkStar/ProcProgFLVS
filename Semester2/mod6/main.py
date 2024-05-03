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
    global questionFrame, answers, page
    questions = ["Question 0", "Question 1", "Question 2"]
    answers = [] # Holds all the answers that the user chose
    page = 0
    currentQuestion = questions[page]
    questionFrame = Frame(master=mainFrame)
    pageIndicator = Label(master=questionFrame, text=f"{page+1}/{len(questions)}")
    questionText = Label(master=questionFrame, text=currentQuestion)
    answerFrame = Frame(master=questionFrame)
    answerButton0 = Button(master=answerFrame, text="Never", command=lambda: answer_clicked(1, questions, questionText, pageIndicator))
    answerButton1 = Button(master=answerFrame, text="Rarely", command=lambda: answer_clicked(2, questions, questionText, pageIndicator))
    answerButton2 = Button(master=answerFrame, text="Occasionally", command=lambda: answer_clicked(3, questions, questionText, pageIndicator))
    answerButton3 = Button(master=answerFrame, text="Frequently", command=lambda: answer_clicked(4, questions, questionText, pageIndicator))
    answerButton4 = Button(master=answerFrame, text="Very Frequently", command=lambda: answer_clicked(5, questions, questionText, pageIndicator))
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

def answer_clicked(answer, questions, questionText, pageIndicator): # Tons of variables. I just didn't want to make them all global...
    """
    Handle changing the page and adding the chosen answer to the list
    """
    global page
    if page == 0:
        answers.append([])
    currentRun = len(answers)-1
    answers[currentRun].append(answer)
    page += 1
    # print(f"Questions: {len(questions)}, Selected Answer: {answer}, Current Page: {page}, Current Run: {currentRun}")
    if page == len(questions):
        page = 0
        switch_to("back", "questionnaire")
        change_question(page, questions, questionText, pageIndicator)
    else:
        change_question(page, questions, questionText, pageIndicator)

def change_question(page, questions, questionText, pageIndicator):
    """
    Handle updating the question, page indicator, and all the answers
    """
    currentQuestion = questions[page]
    pageIndicator.configure(text=f"{page+1}/{len(questions)}")
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
    global coursesFrame
    coursesFrame = Frame(master=mainFrame)

def switch_to(string, location=False):
    """
    Used to switch between menus (from the main menu to others and back)
    """
    match string:
        case "questionnaire":
            mainMenuFrame.forget()
            try:
                if len(answers[len(answers)-1]) == 1:
                    page = 0
            except IndexError:
                pass
            questionFrame.pack()
        case "research":
            mainMenuFrame.forget()
            researchFrame.pack()
        case "courses":
            mainMenuFrame.forget()
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

main()