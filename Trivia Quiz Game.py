import tkinter as tk
from tkinter import messagebox

# Quiz questions
questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Venus", "Mars", "Jupiter"], "answer": "Mars"},
    {"question": "Who wrote 'Harry Potter'?", "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Agatha Christie"], "answer": "J.K. Rowling"}
]

class TriviaQuiz:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Trivia Quiz")

        self.question_label = tk.Label(self.window, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.window, text="", font=("Arial", 14), width=20, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.score = 0
        self.current_question = 0
        self.load_question()

        self.window.mainloop()

    def load_question(self):
        question_data = questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        for i, option in enumerate(question_data["options"]):
            self.buttons[i].config(text=option)

    def check_answer(self, index):
        if questions[self.current_question]["options"][index] == questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Over", f"Your Score: {self.score}/{len(questions)}")
            self.window.destroy()

TriviaQuiz()