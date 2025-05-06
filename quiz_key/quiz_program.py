#import tkinter and random
import tkinter as tk
from tkinter import messagebox
import random

#define the quizgame class
class QuizGame:
    def __init__(self, root):
    #display intro screen with start button
        self.root = root
        self.root.title("Object-Oriented Programming Quiz")
        self.root.geometry("700x500")
        self.root.config(bg="#EAE0D5")
        #load quiz questions
        #display quiz questions
        #show question one at a time
        self.score = 0
        self.question_index = 0
        self.questions = self.load_questions()
        random.shuffle(self.questions)
        self.is_paused = False
    
        self.create_start_screen()

#read the quiz txt
#parse each bock: question, options, and the correct answer
#append to questions list
#create centered title and start button
#display the questions and options
#display pause, exit, and disabled next button
#bottom frame with controls
#disable all answer buttons
#green for correct, red for wrong
#enable next button
#pause: freeze the screen and show message
#resume: continue the quiz
#show congratulations message
#display the score and add restart/exit buttons
#launch the quiz