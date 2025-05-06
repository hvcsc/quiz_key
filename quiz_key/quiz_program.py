#import tkinter and random
import tkinter as tk
from tkinter import (messagebox)
import random

#define the quizgame class
class QuizGame:
    def __init__(self, root):
    #display intro screen with start button
        self.root = root
        self.root.title("Object-Oriented Programming Quiz")
        self.root.geometry("700x500")
        self.root.config(bg = "#EAE0D5")
        #load quiz questions
        #display quiz questions
        #show question one at a time
        self.score = 0
        self.question_index = 0
        self.questions = self.load_questions()
        random.shuffle(self.questions)
        self.is_paused = False

        self.create_start_screen()

    def load_questions(self):
        questions = []
        try:
            #read the quiz txt
            with open("quiz_key.txt", "r") as file:
                content = file.read().strip().split("\n\n")
                #parse each bock: question, options, and the correct answer
                #append to questions list
                for block in content:
                    lines = block.strip().split("\n")
                    question = lines[0]
                    choices = {
                        'a': lines[1][3:].strip(),
                        'b': lines[2][3:].strip(),
                        'c': lines[3][3:].strip(),
                        'd': lines[4][3:].strip()
                    }
                    answer = lines[5].split(":")[1].strip()
                    questions.append({
                        "question": question,
                        "choices": choices,
                        "answer": answer
                    })
        except FileNotFoundError:
            messagebox.showerror("Error", "quiz_key.txt not found!")
        return questions

    #create centered title and start button
    def create_start_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.root, bg = "#EAE0D5")
        frame.place(relx = 0.5, rely = 0.5, anchor = "center")

        title_label = tk.Label(frame, text = "Object-Oriented Programming Quiz", font = ("Times New Roman", 24, "bold"), bg = "#EAE0D5", fg = "#22333B")
        title_label.pack(pady = 20)

        start_button = tk.Button(frame, text = "Start", command = self.start_quiz, font = ("Times New Roman", 16), bg = "#C6AC8E", fg = "#0A0908", width = 12)
        start_button.pack()

    def start_quiz(self):
        self.score = 0
        self.question_index = 0
        self.clear_screen()
        self.display_question()

    #display the questions and options
    def display_question(self):
        self.clear_screen()

        if self.question_index >= len(self.questions):
            self.show_score()
            return

        current_question = self.questions[self.question_index]

        self.top_frame = tk.Frame(self.root, bg = "#EAE0D5")
        self.top_frame.pack(expand = True)

        self.question_label = tk.Label(
            self.top_frame,
            text = current_question["question"],
            font = ("Times New Roman", 18),
            wraplength = 600,
            justify = "center",
            bg = "#EAE0D5",
            fg = "#22333B"
        )
        self.question_label.pack(pady = 10)

        self.answer_buttons = []
        for key in ['a', 'b', 'c', 'd']:
            btn = tk.Button(
                self.top_frame,
                text = f"{key}.{current_question['choices'][key]}",
                font = ("Times New Roman", 14),
                bg = "#C6AC8E",
                width = 40,
                command = lambda k = key: self.check_answer(k)
            )
            btn.pack(pady = 5)
            self.answer_buttons.append((key, btn))

        #display pause, exit, and disabled next button
        #bottom frame with controls
        self.bottom_frame = tk.Frame(self.root, bg = "#EAE0D5")
        self.bottom_frame.pack(side = "bottom", pady = 20)

        self.pause_button = tk.Button(
            self.bottom_frame,
            text = "Pause",
            font = ("Times New Roman", 12),
            bg = "#C6AC8E",
            fg = "#0A0908",
            command = self.toggle_pause
        )
        self.pause_button.pack(side = "left", padx = 20)

        self.next_button = tk.Button(
            self.bottom_frame,
            text = "Next",
            font = ("Times New Roman", 12),
            bg = "#C6AC8E",
            fg = "#0A0908",
            command = self.next_question,
            state = "disabled"
        )
        self.next_button.pack(side = "left", padx = 20)

        self.exit_button = tk.Button(
            self.bottom_frame,
            text = "Exit",
            font = ("Times New Roman", 12),
            bg = "#5E503F",
            fg = "white",
            command = self.root.quit
        )
        self.exit_button.pack(side = "right", padx = 20)

    #disable all answer buttons
    #green for correct, red for wrong
    def check_answer(self, selected):
        if self.is_paused:
            return

        correct = self.questions[self.question_index]["answer"]
        for key, btn in self.answer_buttons:
            btn.config(state = "disabled")
            if key == correct:
                btn.config(bg = "lightgreen")
            elif key == selected:
                btn.config(bg = "salmon")

        if selected == correct:
            self.score += 1

        self.next_button.config(state="normal")

    #enable next button
    def next_question(self):
        self.question_index += 1
        self.display_question()

#pause: freeze the screen and show message
#resume: continue the quiz
#show congratulations message
#display the score and add restart/exit buttons
#launch the quiz