import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")

        self.board = [""] * 9
        self.current_player = "X"

        self.buttons = [tk.Button(self.window, text="", font=("Arial", 20), height=2, width=5, 
                                  command=lambda i=i: self.make_move(i)) 
                        for i in range(9)]
        
        for i in range(9):
            row, col = divmod(i, 3)
            self.buttons[i].grid(row=row, column=col)

        self.window.mainloop()

    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.destroy()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.destroy()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(self.board[a] == self.board[b] == self.board[c] != "" for a, b, c in winning_combinations)

TicTacToe()