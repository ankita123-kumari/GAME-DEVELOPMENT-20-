import tkinter as tk
import random

class RPGGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text-Based RPG")

        self.story_label = tk.Label(self.root, text="You wake up in a mysterious forest...", font=("Arial", 14), wraplength=400)
        self.story_label.pack()

        self.choice_button1 = tk.Button(self.root, text="Explore deeper", command=self.explore, font=("Arial", 14))
        self.choice_button1.pack()

        self.choice_button2 = tk.Button(self.root, text="Stay put", command=self.rest, font=("Arial", 14))
        self.choice_button2.pack()

        self.stats_label = tk.Label(self.root, text="HP: 100 | Level: 1", font=("Arial", 12))
        self.stats_label.pack()

        self.player_hp = 100
        self.level = 1
        self.inventory = ["Health Potion"]

        self.root.mainloop()

    def update_stats(self):
        self.stats_label.config(text=f"HP: {self.player_hp} | Level: {self.level}")

    def explore(self):
        event = random.choice(["You find treasure!", "A goblin appears!", "You discover an ancient ruin!"])
        self.story_label.config(text=event)

        if event == "A goblin appears!":
            self.battle()
        elif event == "You find treasure!":
            self.inventory.append("Gold Coin")

    def rest(self):
        self.player_hp = min(100, self.player_hp + 10)
        self.story_label.config(text="You rest and regain some health.")
        self.update_stats()

    def battle(self):
        goblin_hp = 30
        while goblin_hp > 0 and self.player_hp > 0:
            goblin_hp -= random.randint(5, 20)
            self.player_hp -= random.randint(5, 15)
        if self.player_hp > 0:
            self.level += 1
            self.story_label.config(text="You defeated the goblin! You leveled up!")
        else:
            self.story_label.config(text="You have been defeated... Game Over!")
        self.update_stats()

if __name__ == "__main__":
    RPGGame()