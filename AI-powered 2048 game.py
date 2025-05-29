import tkinter as tk
import numpy as np
import random

SIZE = 4
COLORS = {0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
          16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
          256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}

class Game2048:
    def __init__(self):
        self.board = np.zeros((SIZE, SIZE), dtype=int)
        self.add_tile()
        self.add_tile()

    def add_tile(self):
        empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.board[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.board[r][c] = 2 if random.random() < 0.9 else 4

    def move_left(self):
        def slide(row):
            row = [x for x in row if x != 0]
            for i in range(len(row) - 1):
                if row[i] == row[i + 1]:
                    row[i] *= 2
                    row[i + 1] = 0
            return [x for x in row if x != 0] + [0] * (SIZE - len(row))

        self.board = np.array([slide(row) for row in self.board])
        self.add_tile()

    def move_right(self):
        self.board = np.flip(self.board, axis=1)
        self.move_left()
        self.board = np.flip(self.board, axis=1)

    def move_up(self):
        self.board = self.board.T
        self.move_left()
        self.board = self.board.T

    def move_down(self):
        self.board = np.flip(self.board.T, axis=1)
        self.move_left()
        self.board = np.flip(self.board.T, axis=1)

    def get_possible_moves(self):
        moves = []
        for move_func in [self.move_left, self.move_right, self.move_up, self.move_down]:
            temp_board = self.board.copy()
            move_func()
            if not np.array_equal(temp_board, self.board):
                moves.append(move_func)
            self.board = temp_board
        return moves

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("2048 AI Game")
        self.cells = [[tk.Label(self.root, width=6, height=3, font=("Helvetica", 24, "bold"), bg=COLORS[0])
                       for _ in range(SIZE)] for _ in range(SIZE)]
        for r, row in enumerate(self.cells):
            for c, cell in enumerate(row):
                cell.grid(row=r, column=c, padx=5, pady=5)
        self.root.bind("<Left>", lambda e: self.make_move(game.move_left))
        self.root.bind("<Right>", lambda e: self.make_move(game.move_right))
        self.root.bind("<Up>", lambda e: self.make_move(game.move_up))
        self.root.bind("<Down>", lambda e: self.make_move(game.move_down))
        self.update_gui()
        self.root.after(500, self.ai_move)
        self.root.mainloop()

    def update_gui(self):
        for r in range(SIZE):
            for c in range(SIZE):
                value = self.game.board[r][c]
                self.cells[r][c].config(text=value if value else "", bg=COLORS.get(value, "#3c3a32"))
    
    def make_move(self, move_func):
        move_func()
        self.update_gui()

    def ai_move(self):
        moves = self.game.get_possible_moves()
        if moves:
            random.choice(moves)()
            self.update_gui()
            self.root.after(500, self.ai_move)

if __name__ == "__main__":
    game = Game2048()
    GUI(game)