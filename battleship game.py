import tkinter as tk
import numpy as np
import random

GRID_SIZE = 5
SHIPS = [(3, "Battleship"), (2, "Destroyer")]
AI_SHOTS = []

class BattleshipGame:
    def __init__(self):
        self.player_board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.ai_board = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.place_ai_ships()
    
    def place_ai_ships(self):
        for size, name in SHIPS:
            placed = False
            while not placed:
                r, c = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
                if c + size <= GRID_SIZE and np.all(self.ai_board[r, c:c+size] == 0):
                    self.ai_board[r, c:c+size] = 1
                    placed = True
    
    def player_attack(self, r, c):
        if self.ai_board[r, c] == 1:
            self.ai_board[r, c] = 2  # Hit
            return True
        return False
    
    def ai_attack(self):
        while True:
            r, c = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if (r, c) not in AI_SHOTS:
                AI_SHOTS.append((r, c))
                return r, c

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Battleship Game")
        
        self.buttons = [[tk.Button(self.root, width=4, height=2, command=lambda r=r, c=c: self.attack(r, c)) 
                         for c in range(GRID_SIZE)] for r in range(GRID_SIZE)]
        for r, row in enumerate(self.buttons):
            for c, btn in enumerate(row):
                btn.grid(row=r, column=c, padx=2, pady=2)
        
        self.status_label = tk.Label(self.root, text="Your Turn!", font=("Arial", 14))
        self.status_label.grid(row=GRID_SIZE, columnspan=GRID_SIZE)
        self.root.mainloop()

    def attack(self, r, c):
        if self.game.player_attack(r, c):
            self.buttons[r][c].config(text="X", bg="red")
        else:
            self.buttons[r][c].config(text="O", bg="blue")

        self.status_label.config(text="AI's Turn...")
        self.root.after(1000, self.ai_turn)

    def ai_turn(self):
        r, c = self.game.ai_attack()
        self.status_label.config(text=f"AI Attacks: {r},{c}")
        self.root.after(1000, lambda: self.status_label.config(text="Your Turn!"))

if __name__ == "__main__":
    game = BattleshipGame()
    GUI(game)