import tkinter as tk
from tkinter import messagebox

class EscapeRoomGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Escape Room Game")

        self.room_label = tk.Label(self.root, text="You're locked in! Solve the puzzles to escape.", font=("Arial", 14))
        self.room_label.pack()

        self.puzzle_button1 = tk.Button(self.root, text="Puzzle 1", command=self.solve_puzzle1, font=("Arial", 14))
        self.puzzle_button1.pack()

        self.puzzle_button2 = tk.Button(self.root, text="Puzzle 2", command=self.solve_puzzle2, font=("Arial", 14))
        self.puzzle_button2.pack()

        self.exit_button = tk.Button(self.root, text="Exit Room", command=self.check_escape, font=("Arial", 14), state="disabled")
        self.exit_button.pack()

        self.puzzle_solved = {"puzzle1": False, "puzzle2": False}
        self.root.mainloop()

    def solve_puzzle1(self):
        answer = tk.simpledialog.askstring("Puzzle 1", "What is 2 + 2?")
        if answer == "4":
            messagebox.showinfo("Correct!", "Puzzle 1 solved!")
            self.puzzle_solved["puzzle1"] = True
            self.check_puzzles()
        else:
            messagebox.showerror("Incorrect!", "Try again!")

    def solve_puzzle2(self):
        answer = tk.simpledialog.askstring("Puzzle 2", "What is the capital of France?")
        if answer.lower() == "paris":
            messagebox.showinfo("Correct!", "Puzzle 2 solved!")
            self.puzzle_solved["puzzle2"] = True
            self.check_puzzles()
        else:
            messagebox.showerror("Incorrect!", "Try again!")

    def check_puzzles(self):
        if all(self.puzzle_solved.values()):
            self.exit_button.config(state="normal")

    def check_escape(self):
        messagebox.showinfo("Congratulations!", "You've escaped the room!")
        self.root.quit()

if __name__ == "__main__":
    EscapeRoomGame()