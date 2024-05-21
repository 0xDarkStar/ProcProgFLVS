from tkinter import *
from datetime import datetime
import webbrowser
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
    questions = {"How often do you explain complex ideas to others in a clear and concise way?": "Communication",
                 "When interacting with others, do you actively listen to understand their point of view?": "Communication",
                 "How comfortable are you presenting information in front of a group?": "Communication",
                 "Do you consider yourself a strong written communicator?": "Communication",
                 "When faced with a problem, how often do you consider multiple perspectives before forming a solution?": "Critical Thinking",
                 "How well can you identify the strengths and weaknesses of an argument?": "Critical Thinking",
                 "How comfortable are you questioning assumptions and challenging conventional thinking?": "Critical Thinking",
                 "How often do you develop creative solutions to problems?": "Problem-solving",
                 "When faced with challenges, do you approach them with a positive and determined attitude?": "Problem-solving",
                 "How well do you break down complex problems into smaller, more manageable steps?": "Problem-solving",
                 "How comfortable are you working effectively with others towards a common goal?": "Teamwork",
                 "When working in a team, how often do you listen to and value the ideas of your teammates?": "Teamwork",
                 "How willing are you to share credit and support your teammates' success?": "Teamwork",
                 "How effective are you at prioritizing tasks and meeting deadlines?": "Time Management",
                 "How often do you plan and schedule your time effectively to complete your work?": "Time Management",
                 "How well do you manage distractions and stay focused on the task at hand?": "Time Management",
                 "How often do you take initiative and complete tasks without needing to be told?": "Work Ethic",
                 "When faced with a challenging task, how often do you persevere until you complete it?": "Work Ethic",
                 "How reliable are you in meeting deadlines and commitments?": "Work Ethic",
                 "How often do you break down complex information into smaller, easier-to-understand parts?": "Analytical Skills",
                 "When presented with data or evidence, how often do you analyze it to identify underlying trends or patterns?": "Analytical Skills",
                 "How comfortable are you evaluating the strengths and weaknesses of different arguments or solutions?": "Analytical Skills",
                 "How often do you actively seek out information from reliable sources to answer questions or solve problems?": "Research Skills",
                 "When researching a topic, how often do you use a variety of resources, such as books, articles, and websites?": "Research Skills",
                 "How comfortable are you evaluating the credibility and relevance of information you find?": "Research Skills",
                 "How often do you carefully proofread your work to ensure there are no errors?": "Attention to Detail",
                 "When completing tasks, how often do you pay close attention to even the smallest details?": "Attention to Detail",
                 "How well do you follow instructions and procedures accurately?": "Attention to Detail",
                 "How often do you build rapport and establish positive relationships with others?": "Interpersonal Skills",
                 "When working with others, how often do you show empathy and understanding of their perspectives?": "Interpersonal Skills",
                 "How comfortable are you communicating effectively with people from different backgrounds?": "Interpersonal Skills",
                 "How often do you take initiative and motivate others to achieve a goal?": "Leadership Skills",
                 "When working in a group, how often do you delegate tasks effectively and ensure everyone is on track?": "Leadership Skills",
                 "How comfortable are you making decisions and inspiring others to follow your lead?": "Leadership Skills",
                 "How often do you effectively communicate your ideas and persuade others to see your point of view?": "Negotiation Skills",
                 "When faced with a disagreement, how often do you find solutions that are acceptable to all parties involved?": "Negotiation Skills",
                 "How comfortable are you advocating for your own interests while also considering the needs of others?": "Negotiation Skills",
                 "How often do you come up with new and original ideas to solve problems?": "Creativity",
                 "When faced with a challenge, how often do you think outside the box and approach it from a different angle?": "Creativity",
                 "How comfortable are you expressing yourself creatively and thinking in unconventional ways?": "Creativity",
                 "How often do you seek out opportunities to learn about different cultures and perspectives?": "Cultural Awareness",
                 "When interacting with people from different backgrounds, how often do you show respect and sensitivity to their cultural norms and values?": "Cultural Awareness",
                 "How comfortable are you adapting your communication style and behavior to different cultural contexts?": "Cultural Awareness",
                 "How often do you feel comfortable working outdoors and in potentially challenging environments?": "Fieldwork",
                 "How often do you enjoy working with data and identifying patterns and trends?": "Data Analysis",
                 "How comfortable are you using tools and techniques to communicate information visually?": "Visualization Skills",
                 "How comfortable are you working in a laboratory setting and following safety protocols?": "Laboratory Skills",
                 "How often do you adjust your approach or thinking based on new information or changing circumstances?": "Adaptability",
                 "How often do you pay close attention to what others are saying and try to understand their point of view?": "Active Listening",
                 "How often can you identify and understand the emotions and feelings of others?": "Empathy",
                 "How often do you break down problems into logical steps and analyze information objectively?": "Logical Thinking",
                 "How comfortable are you learning and using programming languages to create software applications?": "Coding Skills",
                 "How often do you enjoy solving problems through code?": "Coding Skills",
                 "How often do you enjoy identifying and fixing errors in software programs?": "Software Testing",
                 "Depending on your specific field, how often do you use specialized equipment or software programs?": "Technical Skills",
                 "How often do you effectively plan, organize, and delegate tasks to complete projects on time and within budget?": "Project Management Skills",
                 "How often do you remain calm and focused when faced with challenges or setbacks?": "Patience",
                 "Depending on your chosen field, how often do you use mathematical concepts and calculations to solve problems?": "Mathematics",
                 "How often do you think strategically about business concepts like marketing, finance, and operations?": "Business Acumen",
                 "How often do you demonstrate compassion and a willingness to help others in need?": "Patient Care",
                 "Depending on your chosen field, how often do you apply scientific principles and theories to understand and explain the world around you?": "Scientific Knowledge",
                 "How often do you require a high degree of manual skill and coordination to perform tasks in your chosen field?": "Dexterity",
                 "Depending on your chosen field, how often do you use foreign languages to communicate or access information?": "Foreign Language"}
    answers = [] # Holds all the answers that the user chose
    page = 0
    questionKeys = list(questions.keys())
    currentQuestion = questionKeys[page]
    questionFrame = Frame(master=mainFrame)
    pageIndicator = Label(master=questionFrame, text=f"{page+1}/{len(questionKeys)}")
    questionText = Label(master=questionFrame, text=currentQuestion, wraplength=400)
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
    if page == 0: # They are starting a new questionnaire
        answers.append([]) # Make the list their answers go into
    currentRun = len(answers)-1 # Set where the current run is (the last list)
    answers[currentRun].append(answer) # Add the chosen answer to the current run
    page += 1 # Move to the next page
    if page == len(questionKeys): # If the page is equal to the length of questionKeys (it is +1 the last index)
        page = 0 # Set the apge back to zero for the next run
        switch_to("back", "questionnaire") # Go back
        change_question(page, questionKeys, questionText, pageIndicator) # Reset the text
        now = datetime.now() # Grab the date and time
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        answers[currentRun].append(date) # Add it to the end of the run
    else: # They haven't reached the end of the questions
        change_question(page, questionKeys, questionText, pageIndicator) # Move to the next question

def change_question(page, questionKeys, questionText, pageIndicator):
    """
    Handle updating the question, page indicator, and all the answers
    """
    currentQuestion = questionKeys[page] # Grab the current question
    pageIndicator.configure(text=f"{page+1}/{len(questionKeys)}") # Change the page indicator
    questionText.configure(text=currentQuestion) # Update the question

def research():
    """
    Make the research page
    """
    global researchFrame
    researchFrame = Frame(master=mainFrame)
    researchText = Label(master=researchFrame, text="Research Questions, Answers, and sources")
    researchQAFrame = Frame(master=researchFrame)
    researchQAs = {"0": {"Question": "What majors can be chosen?",
                         "Answer": "A lot of majors can be chosen such as computer programming, education, law, and finance.",
                         "Source": False,
                         "Link": "https://www.mymajors.com/college-majors/"},
                   "1": {"Question": "What do the jobs that those majors lead to entail.",
                         "Answer": "Almost all if not all of the jobs use computers for work, require you to be good at math, and work with others.",
                         "Source": False,
                         "Link": "https://www.careerexplorer.com"},
                   "2": {"Question": "How do I plan to execute the project?",
                         "Answer": "I will choose a platform that it will work on, find/think of problems that might occur during creation/execution, and make sure to add tons of comments (when necessary) to make the code easier to understand. In the end, I learned that there is a lot more to the SDLC than just planning, creation, then release.",
                         "Source": False,
                         "Link": "https://resources.github.com/software-development/what-is-sdlc/"}}
    makeResearchQAs(researchQAs, researchQAFrame)
    backButton = Button(master=researchFrame, text="Go Back", command=lambda: switch_to("back", "research"))
    researchText.pack()
    researchQAFrame.pack()
    backButton.pack()

def makeResearchQAs(researchQAs, researchQAFrame):
    for i in range(0,3):
        for ii in range(0,2):
            iii = list(researchQAs["0"].keys())[ii]
            researchQAs[str(i)][iii] = Label(master=researchQAFrame, text=researchQAs[str(i)][iii], wraplength=400)
            researchQAs[str(i)][iii].grid(column=ii, row=i, pady=5)
        researchQAs[str(i)]["Source"] = Button(master=researchQAFrame, text=researchQAs[str(i)]["Link"], relief=FLAT ,command=lambda link=researchQAs[str(i)]["Link"]: webbrowser.open(link))
        researchQAs[str(i)]["Source"].grid(column=2, row=i, pady=5)

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
        attemptQADict[i] = [Label(master=QAFrame, text=list(questions.keys())[i], relief="sunken", width=30, height=4, wraplength=230), Label(master=QAFrame, text="Answer", relief="sunken", width=15, height=4)]
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
                attemptsList.delete(0,END) # Clear the old attempts list
                for i in answers:
                    attemptString = f"Attempt {attemptIndex}, {i[-1]}" # Make the string that will be displayed to the user
                    attemptsList.insert(attemptIndex, attemptString) # Add the string and index of the attempt
                    attemptIndex += 1
            else: # They haven't done the questionnaire yet
                mainText.configure(text="You have not completed the questionnaire yet.")
            coursesFrame.pack()
        case "attempt":
            if len(attemptIndex) > 0: # They chose an attempt that exists
                try:
                    mainText.configure(text="All attempts of the questionnaire:")
                    coursesFrame.forget()
                    attemptText.configure(text=f"Attempt number: {attemptIndex[0]+1}\nDate taken: {answers[attemptIndex[0]][-1]}")
                    # Update all answers in the QAFrame to be accurate
                    index = 0
                    answerConvert = ["Never", "Rarely", "Occasionally", "Often", "Very Often"]
                    for i in list(questions.keys()): # Update the questions and the answers to match the attempt shown
                        currentAnswer = answers[attemptIndex[0]][index] # Grab the current answer
                        attemptQADict[index][0].configure(text=i) # Update the question
                        attemptQADict[index][1].configure(text=answerConvert[currentAnswer-1]) # Update the answer
                        index += 1
                    topMajorsParts[0]["canvas"].create_rectangle(0, 0, 50, 5, fill="green") # Percentage match bar (replace 50 with the percentage)
                    topMajorsParts[0]["match"].configure(text="50% match") # Percentage match text (replace the 50 with the percentage)
                    attemptFrame.pack()
                except IndexError: # They most likely didn't finish the attempt
                    attemptFrame.forget() # Close that frame
                    coursesFrame.pack() # Reopen this one
                    mainText.configure(text="You didn't complete this attempt.") # Tell them why it didn't work.
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
    majors = {"Template": ["Description", ["List", "Of", "Career", "Paths"], [Communication, Critical Thinking, Problem-solving, Teamwork, Time Management, Work Ethic, Analytical Skills, Research Skills, Attention to Detail, Interpersonal Skills, Leadership skills, Negotiation Skills, Creativity, Cultural Awareness]],
            "Example": ["Often does X, Y, and Z. Has to ... often.", ["Job1", "Job2", "Job3", "Job4"], [5, 3, 3, ...]]}
    """
    majors = {
              "Geology": {
                          "Description": "Studies the Earth's composition, structure, and processes that shape it.\nGeology majors gain a strong foundation in earth science, with skills in critical thinking, data analysis, and problem-solving. They explore topics like climate change, resource exploration, and natural hazards.",
                          "Jobs": ["Geologist", "Environmental Consultant", "Hydrogeoligist", "Petroleum, Geoligist", "Oceanographer"],
                          "Skills": {"Communication": 3,
                                     "Critical Thinking": 5,
                                     "Problem-solving": 5,
                                     "Teamwork": 3,
                                     "Time Management": 3,
                                     "Work Ethic": 4,
                                     "Analytical Skills": 5,
                                     "Research Skills": 4,
                                     "Attention to Detail": 4,
                                     "Interpersonal Skills": 2,
                                     "Leadership Skills": 2,
                                     "Negotiation Skills": 1,
                                     "Creativity": 2,
                                     "Cultural Awareness": 2},
                          "Preferred": ["Fieldwork", "Data Analysis", "Visualization Skills"]},
              "Biology": {
                          "Description": "Focuses on living organisms, their structure, function, and interactions with the environment.\nBiology majors develop strong analytical, research, and communication skills. They delve into diverse areas like genetics, cell biology, and ecology.",
                          "Jobs": ["Biologist", "Medical Researcher", "Environmental Scientist", "Marine Bioligist", "Biotechnologist"],
                          "Skills": {"Communication": 3,
                                     "Critical Thinking": 4,
                                     "Problem-solving": 4,
                                     "Teamwork": 4,
                                     "Time Management": 3,
                                     "Work Ethic": 4,
                                     "Analytical Skills": 4,
                                     "Research Skills": 4,
                                     "Attention to Detail": 4,
                                     "Interpersonal Skills": 3,
                                     "Leadership Skills": 2,
                                     "Negotiation Skills": 1,
                                     "Creativity": 3,
                                     "Cultural Awareness": 2},
                          "Preferred": ["Laboratory Skills", "Adaptability"]},
              "Psychology": {
                             "Description": "Explores human behavior, thoughts, and emotions.\nPsychology majors hone their critical thinking, research, and communication skills. They study mental processes, social interactions, and psychological disorders.",
                             "Jobs": ["Clinical Psychologist", "Counseling Psychologist", "School Psychologist", "Industrial/Organizational Psychologist", "Social Worker"],
                             "Skills": {"Communication": 4,
                                        "Critical Thinking": 5,
                                        "Problem-solving": 4,
                                        "Teamwork": 3,
                                        "Time Management": 3,
                                        "Work Ethic": 4,
                                        "Analytical Skills": 4,
                                        "Research Skills": 4,
                                        "Attention to Detail": 3,
                                        "Interpersonal Skills": 4,
                                        "Leadership Skills": 2,
                                        "Negotiation Skills": 2,
                                        "Creativity": 3,
                                        "Cultural Awareness": 3},
                             "Preferred": ["Empathy"]},
              "Computer Science": {
                                   "Description": "The theoretical foundation of computing and software development.\nComputer Science majors develop strong analytical and problem-solving skills. They learn algorithms, data structures, and programming languages to design and build software applications.",
                                   "Jobs": ["Software Developer", "Web Developer", "Systems Engineer", "Database Administrator", "Data Scientist"],
                                   "Skills": {"Communication": 3,
                                              "Critical Thinking": 5,
                                              "Problem-solving": 5,
                                              "Teamwork": 4,
                                              "Time Management": 3,
                                              "Work Ethic": 4,
                                              "Analytical Skills": 5,
                                              "Research Skills": 3,
                                              "Attention to Detail": 5,
                                              "Interpersonal Skills": 3,
                                              "Leadership Skills": 2,
                                              "Negotiation Skills": 1,
                                              "Creativity": 3,
                                              "Cultural Awareness": 2},
                                   "Preferred": ["Logical Thinking", "Coding Skills"]},
              "Computer Programming": {
                                       "Description": "The practical application of computer science principles to create software programs.\nComputer programmers excel in problem-solving, attention to detail, and critical thinking. They focus on writing code, debugging errors, and implementing software solutions.",
                                       "Jobs": ["Back-end Developer", "Front-end Developer", "Game Developer", "Full Stack Developer", "Software Engineer"],
                                       "Skills": {"Communication": 3,
                                                  "Critical Thinking": 5,
                                                  "Problem-solving": 5,
                                                  "Teamwork": 4,
                                                  "Time Management": 3,
                                                  "Work Ethic": 4,
                                                  "Analytical Skills": 5,
                                                  "Research Skills": 2,
                                                  "Attention to Detail": 5,
                                                  "Interpersonal Skills": 3,
                                                  "Leadership Skills": 2,
                                                  "Negotiation Skills": 1,
                                                  "Creativity": 3,
                                                  "Cultural Awareness": 2},
                                       "Preferred": ["Logical Thinking", "Coding Skills", "Software Testing"]},
              "Engineering": {
                              "Description": "A broad discipline encompassing various branches like mechanical, electrical, and computer engineering.\nEngineers excel in critical thinking, problem-solving, and analytical skills. They design, develop, and implement solutions to complex technical challenges.",
                              "Jobs": ["Civil Engineer", "Mechanical Engineer", "Electrical Engineer", "Aerospace Engineer", "Chemical Engineer"],
                              "Skills": {"Communication": 4,
                                         "Critical Thinking": 5,
                                         "Problem-solving": 5,
                                         "Teamwork": 4,
                                         "Time Management": 4,
                                         "Work Ethic": 4,
                                         "Analytical Skills": 5,
                                         "Research Skills": 3,
                                         "Attention to Detail": 4,
                                         "Interpersonal Skills": 3,
                                         "Leadership Skills": 3,
                                         "Negotiation Skills": 2,
                                         "Creativity": 4,
                                         "Cultural Awareness": 3},
                              "Preferred": ["Technical Skills", "Project Management Skills"]},
              "Education": {
                            "Description": "Provides a foundation for teaching various subjects and age groups. \nEducation majors develop strong communication, interpersonal, and problem-solving skills to create engaging learning environments and cater to diverse student needs.",
                            "Jobs": ["High School Teacher", "Elementary School Teacher", "Special Education Teacher", "School Counselor", "Curriculum Developer"],
                            "Skills": {"Communication": 4,
                                       "Critical Thinking": 4,
                                       "Problem-solving": 4,
                                       "Teamwork": 3,
                                       "Time Management": 4,
                                       "Work Ethic": 4,
                                       "Analytical Skills": 3,
                                       "Research Skills": 3,
                                       "Attention to Detail": 3,
                                       "Interpersonal Skills": 5,
                                       "Leadership Skills": 3,
                                       "Negotiation Skills": 2,
                                       "Creativity": 4,
                                       "Cultural Awareness": 4},
                            "Preferred": ["Patience", "Adaptability"]},
              "Business": {
                           "Description": "A broad field encompassing various areas like marketing, finance, and management.\nBusiness majors develop strong communication, analytical, and problem-solving skills to navigate complex business challenges and make strategic decisions.",
                           "Jobs": ["Marketing Manager", "Project Manager", "Management Consultant", "Human Resources Specialist", "Operations Manager"],
                           "Skills": {"Communication": 4,
                                      "Critical Thinking": 4,
                                      "Problem-solving": 4,
                                      "Teamwork": 4,
                                      "Time Management": 4,
                                      "Work Ethic": 4,
                                      "Analytical Skills": 4,
                                      "Research Skills": 3,
                                      "Attention to Detail": 3,
                                      "Interpersonal Skills": 4,
                                      "Leadership Skills": 3,
                                      "Negotiation Skills": 3,
                                      "Creativity": 3,
                                      "Cultural Awareness": 3},
                           "Preferred": [None]},
              "Finance": {
                          "Description": "Specializes in financial analysis, investment strategies, and risk management.\nFinance majors excel in critical thinking, analytical skills, and attention to detail. They develop expertise in financial modeling, data analysis, and financial markets.",
                          "Jobs": ["Investment Banker", "Financial Advisor", "Financial Analyst", "Commercial Loan Officer", "Risk Analyst"],
                          "Skills": {"Communication": 4,
                                     "Critical Thinking": 5,
                                     "Problem-solving": 5,
                                     "Teamwork": 3,
                                     "Time Management": 4,
                                     "Work Ethic": 4,
                                     "Analytical Skills": 5,
                                     "Research Skills": 4,
                                     "Attention to Detail": 5,
                                     "Interpersonal Skills": 3,
                                     "Leadership Skills": 3,
                                     "Negotiation Skills": 4,
                                     "Creativity": 3,
                                     "Cultural Awareness": 3},
                          "Preferred": ["Mathematics", "Business Acumen"]},
              "Medical": {
                          "Description": "Prepares students for careers in healthcare delivery and patient care.\nMedical fields require strong communication, critical thinking, and teamwork skills. Majors gain a foundation in human biology, medical procedures, and ethical considerations in healthcare.",
                          "Jobs": ["Physician", "Registered Nurse", "Physician Assistant", "Medical Laboratory Scientist", "Physical Therapist"],
                          "Skills": {"Communication": 4,
                                     "Critical Thinking": 5,
                                     "Problem-solving": 5,
                                     "Teamwork": 4,
                                     "Time Management": 4,
                                     "Work Ethic": 5,
                                     "Analytical Skills": 5,
                                     "Research Skills": 4,
                                     "Attention to Detail": 5,
                                     "Interpersonal Skills": 4,
                                     "Leadership Skills": 3,
                                     "Negotiation Skills": 2,
                                     "Creativity": 3,
                                     "Cultural Awareness": 4},
                          "Preferred": ["Patient Care", "Scientific Knowledge", "Dexterity"]},
              "History": {
                          "Description": "Studies past events and their impact on the present.\nHistory majors develop strong research, critical thinking, and communication skills. They learn to analyze historical data, evaluate sources, and interpret historical events from diverse perspectives.",
                          "Jobs": ["Historian", "Archivist", "Museum Curator", "Local Historian", "Historic Preservationist"],
                          "Skills": {"Communication": 4,
                                     "Critical Thinking": 5,
                                     "Problem-solving": 4,
                                     "Teamwork": 3,
                                     "Time Management": 4,
                                     "Work Ethic": 4,
                                     "Analytical Skills": 5,
                                     "Research Skills": 5,
                                     "Attention to Detail": 4,
                                     "Interpersonal Skills": 3,
                                     "Leadership Skills": 2,
                                     "Negotiation Skills": 1,
                                     "Creativity": 4,
                                     "Cultural Awareness": 4},
                          "Preferred": ["Empathy", "Foreign Language"]},
              "Law": {
                      "Description": "Focuses on legal analysis, argumentation, and the application of law to various situations.\nLaw students hone their critical thinking, research, and communication skills to excel in legal research, writing, and advocacy.",
                      "Jobs": ["Lawyer", "Judge", "Paralegal", "Compliance Officer", "Legal Journalist/Writer"],
                      "Skills": {"Communication": 5,
                                 "Critical Thinking": 5,
                                 "Problem-solving": 5,
                                 "Teamwork": 4,
                                 "Time Management": 4,
                                 "Work Ethic": 4,
                                 "Analytical Skills": 5,
                                 "Research Skills": 5,
                                 "Attention to Detail": 5,
                                 "Interpersonal Skills": 4,
                                 "Leadership Skills": 3,
                                 "Negotiation Skills": 5,
                                 "Creativity": 3,
                                 "Cultural Awareness": 3},
                      "Preferred": [None]}
    }
    scores = {
              "Geology": 0,
              "Biology": 0,
              "Psychology": 0,
              "Computer Science": 0,
              "Computer Programming": 0,
              "Engineering": 0,
              "Education": 0,
              "Business": 0,
              "Finance": 0,
              "Medical": 0,
              "History": 0,
              "Law": 0
    }
    """
    The algorithm for recommending courses (as far as I've planned), will recommend based on the difference between set points and chosen answers.

    That can be done by checking an answer, using the index of the answer to find out what skill it is related to, then going through all the majors' to subtract against that one skill, adding each result to a list.
    Said list will have an integer in it for each major. That integer is what is added to by each result (according to the major). Before adding a result though, make sure that the result is positive (make it absolute).

    It could recommend the top three courses or only the course(s) that match the most.
    """
    # Grab all the questions and order (put in lists) the answers based on skill
    # Find the average of each skill (go through each list and find the average)
    # Save a separate score for each major in a dict

main()
