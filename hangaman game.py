import tkinter as tk
import random

# Word list
word_list = ["python", "hangman", "developer", "gaming", "computer"]
word = random.choice(word_list)
guesses = set()
max_attempts = 6

class HangmanGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Hangman Game")

        self.word_label = tk.Label(self.window, text=self.get_display_word(), font=("Arial", 20))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.window, font=("Arial", 16))
        self.entry.pack(pady=10)

        self.submit_btn = tk.Button(self.window, text="Guess", font=("Arial", 14), command=self.check_guess)
        self.submit_btn.pack(pady=5)

        self.status_label = tk.Label(self.window, text=f"Attempts left: {max_attempts}", font=("Arial", 16))
        self.status_label.pack(pady=10)

        self.window.mainloop()

    def get_display_word(self):
        return " ".join([letter if letter in guesses else "_" for letter in word])

    def check_guess(self):
        global max_attempts
        guess = self.entry.get().lower()

        if guess in word:
            guesses.add(guess)
        else:
            max_attempts -= 1
        
        self.word_label.config(text=self.get_display_word())
        self.status_label.config(text=f"Attempts left: {max_attempts}")

        if "_" not in self.get_display_word():
            self.status_label.config(text="You Win!")
            self.window.destroy()
        elif max_attempts == 0:
            self.status_label.config(text=f"You Lose! Word was '{word}'")
            self.window.destroy()

HangmanGame()