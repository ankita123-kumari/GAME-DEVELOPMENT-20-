import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multiplayer Tic-Tac-Toe")
        
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        self.buttons = [[tk.Button(self.root, text="", width=6, height=3, font=("Arial", 24),
                                   command=lambda r=r, c=c: self.make_move(r, c))
                         for c in range(3)] for r in range(3)]
        
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].grid(row=r, column=c)

        self.status_label = tk.Label(self.root, text="Player X's turn", font=("Arial", 16))
        self.status_label.grid(row=3, columnspan=3)

        self.root.mainloop()

    def make_move(self, r, c):
        if not self.board[r][c] and not self.check_winner():
            self.board[r][c] = self.current_player
            self.buttons[r][c].config(text=self.current_player)
            
            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} Wins!")
            elif all(self.board[r][c] for r in range(3) for c in range(3)):
                self.status_label.config(text="It's a Tie!")
            else:
                self.current_player = "X" if self.current_player == "O" else "O"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0]:
                return True

        for c in range(3):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] and self.board[0][c]:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0]:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2]:
            return True

        return False

if __name__ == "__main__":
    TicTacToe()