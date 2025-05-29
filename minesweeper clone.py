import tkinter as tk
import random

GRID_SIZE = 8
NUM_MINES = 10

class Minesweeper:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Minesweeper")

        self.board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.buttons = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.mines = set()

        self.place_mines()
        self.calculate_numbers()

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                btn = tk.Button(self.window, width=3, height=2, font=("Arial", 14),
                                command=lambda i=i, j=j: self.reveal(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        self.window.mainloop()

    def place_mines(self):
        while len(self.mines) < NUM_MINES:
            i, j = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
            if (i, j) not in self.mines:
                self.mines.add((i, j))
                self.board[i][j] = -1  # -1 represents a mine

    def calculate_numbers(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.board[i][j] == -1:
                    continue
                count = sum((x, y) in self.mines for x in range(i-1, i+2) for y in range(j-1, j+2) if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE)
                self.board[i][j] = count

    def reveal(self, i, j):
        if (i, j) in self.mines:
            self.buttons[i][j].config(text="💣", fg="red")
            self.window.title("Game Over! You hit a mine!")
        else:
            self.buttons[i][j].config(text=str(self.board[i][j]), fg="black")

Minesweeper()