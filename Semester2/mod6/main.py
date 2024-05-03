from tkinter import *

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
    global questionFrame, answers, page
    questions = {"Question 0": ["Answer 0", "Answer 1", "Answer 2", "Answer 3"],
                 "Question 1": ["Answer 4", "Answer 5", "Answer 6", "Answer 8"]}
    answers = [] # Holds all the answers that the user chose
    page = 0
    questionKeys = list(questions.keys())
    currentQuestion = questionKeys[page]
    questionFrame = Frame(master=mainFrame)
    pageIndicator = Label(master=questionFrame, text=f"{page+1}/{len(questionKeys)}")
    questionText = Label(master=questionFrame, text=currentQuestion)
    answerFrame = Frame(master=questionFrame)
    answerButton0 = Button(master=answerFrame, text=questions[currentQuestion][0], command=lambda: answer_clicked(0, questions, questionKeys, questionText, answerButton0, answerButton1, answerButton2, answerButton3, pageIndicator))
    answerButton1 = Button(master=answerFrame, text=questions[currentQuestion][1], command=lambda: answer_clicked(1, questions, questionKeys, questionText, answerButton0, answerButton1, answerButton2, answerButton3, pageIndicator))
    answerButton2 = Button(master=answerFrame, text=questions[currentQuestion][2], command=lambda: answer_clicked(2, questions, questionKeys, questionText, answerButton0, answerButton1, answerButton2, answerButton3, pageIndicator))
    answerButton3 = Button(master=answerFrame, text=questions[currentQuestion][3], command=lambda: answer_clicked(3, questions, questionKeys, questionText, answerButton0, answerButton1, answerButton2, answerButton3, pageIndicator))
    backButton = Button(master=questionFrame, text="Go Back", command=lambda: switch_to("back", "questionnaire"))
    pageIndicator.pack()
    questionText.pack()
    answerButton0.pack(side=LEFT)
    answerButton1.pack(side=LEFT)
    answerButton2.pack(side=LEFT)
    answerButton3.pack(side=LEFT)
    answerFrame.pack()
    backButton.pack()

def answer_clicked(answer, questions, questionKeys, questionText, answerButton0, answerButton1, answerButton2, answerButton3, pageIndicator): # Tons of variables. I just didn't want to make them all global...
    global page
    if page == 0:
        answers.append([])
    currentRun = len(answers)-1
    answers[currentRun].append(answer)
    page += 1
    # print(f"Questions: {len(questionKeys)}, Selected Answer: {answer}, Current Page: {page}, Current Run: {currentRun}")
    if page == len(questionKeys):
        page = 0
        switch_to("back", "questionnaire")
        change_question(page, questions, questionKeys, questionText, answerButton0, answerButton1, answerButton2, answerButton3, pageIndicator)
    else:
        change_question(page, questions, questionKeys, questionText, answerButton0, answerButton1, answerButton2, answerButton3, pageIndicator)

def change_question(page, questions, questionKeys, questionText, answerButton0, answerButton1, answerButton2, answerButton3, pageIndicator):
    currentQuestion = questionKeys[page]
    pageIndicator.configure(text=f"{page+1}/{len(questionKeys)}")
    questionText.configure(text=currentQuestion)
    answerButton0.configure(text=questions[currentQuestion][0])
    answerButton1.configure(text=questions[currentQuestion][1])
    answerButton2.configure(text=questions[currentQuestion][2])
    answerButton3.configure(text=questions[currentQuestion][3])

def research():
    global researchFrame
    researchFrame = Frame(master=mainFrame)

def courses():
    global coursesFrame
    coursesFrame = Frame(master=mainFrame)

def switch_to(string, location=False):
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