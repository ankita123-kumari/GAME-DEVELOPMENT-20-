import tkinter as tk
import numpy as np
import random

ROWS, COLS = 6, 7
PLAYER, AI = 1, 2

class Connect4:
    def __init__(self):
        self.board = np.zeros((ROWS, COLS), dtype=int)

    def drop_piece(self, col, player):
        for row in reversed(range(ROWS)):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return row, col
        return None
    
    def check_win(self, player):
        for row in range(ROWS):
            for col in range(COLS - 3):
                if np.all(self.board[row, col:col+4] == player):
                    return True

        for row in range(ROWS - 3):
            for col in range(COLS):
                if np.all(self.board[row:row+4, col] == player):
                    return True

        for row in range(ROWS - 3):
            for col in range(COLS - 3):
                if all(self.board[row+i, col+i] == player for i in range(4)) or \
                   all(self.board[row+3-i, col+i] == player for i in range(4)):
                    return True
        return False

    def ai_move(self):
        valid_columns = [c for c in range(COLS) if self.board[0][c] == 0]
        return random.choice(valid_columns) if valid_columns else None

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Connect 4")
        self.buttons = [tk.Button(self.root, text="Drop", command=lambda c=c: self.player_move(c)) for c in range(COLS)]
        for c, btn in enumerate(self.buttons):
            btn.grid(row=0, column=c)
        self.cells = [[tk.Label(self.root, width=6, height=3, bg="white", relief="solid")
                       for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c].grid(row=r+1, column=c)
        self.status_label = tk.Label(self.root, text="Your turn!", font=("Arial", 14))
        self.status_label.grid(row=ROWS+1, columnspan=COLS)
        self.root.mainloop()

    def player_move(self, col):
        result = self.game.drop_piece(col, PLAYER)
        if result:
            row, col = result
            self.cells[row][col].config(bg="red")
            if self.game.check_win(PLAYER):
                self.status_label.config(text="You Win!")
                return
            self.root.after(500, self.ai_move)

    def ai_move(self):
        col = self.game.ai_move()
        if col is not None:
            result = self.game.drop_piece(col, AI)
            if result:
                row, col = result
                self.cells[row][col].config(bg="yellow")
                if self.game.check_win(AI):
                    self.status_label.config(text="AI Wins!")

if __name__ == "__main__":
    game = Connect4()
    GUI(game)