import random
import tkinter as tk

# Card values for Blackjack
CARD_VALUES = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
               "J": 10, "Q": 10, "K": 10, "A": 11}

class Blackjack:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        self.start_game()

    def create_deck(self):
        return [rank for rank in CARD_VALUES.keys()] * 4

    def draw_card(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))

    def start_game(self):
        random.shuffle(self.deck)
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.dealer_hand = [self.draw_card(), self.draw_card()]

    def hand_value(self, hand):
        value = sum(CARD_VALUES[card] for card in hand)
        aces = hand.count("A")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def player_hit(self):
        if not self.game_over:
            self.player_hand.append(self.draw_card())
            if self.hand_value(self.player_hand) > 21:
                self.game_over = True
                return "Bust! Dealer wins."
        return ""

    def dealer_turn(self):
        while self.hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.draw_card())
        self.game_over = True
        player_score, dealer_score = self.hand_value(self.player_hand), self.hand_value(self.dealer_hand)
        if dealer_score > 21 or player_score > dealer_score:
            return "You win!"
        elif dealer_score == player_score:
            return "It's a tie!"
        else:
            return "Dealer wins."

class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Blackjack")
        
        self.player_label = tk.Label(self.root, text=f"Player: {self.game.player_hand}", font=("Arial", 14))
        self.player_label.pack()

        self.dealer_label = tk.Label(self.root, text=f"Dealer: [{self.game.dealer_hand[0]}, ?]", font=("Arial", 14))
        self.dealer_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 16), fg="red")
        self.result_label.pack()

        self.hit_button = tk.Button(self.root, text="Hit", command=self.player_hit, font=("Arial", 14))
        self.hit_button.pack()

        self.stand_button = tk.Button(self.root, text="Stand", command=self.dealer_turn, font=("Arial", 14))
        self.stand_button.pack()

        self.root.mainloop()

    def player_hit(self):
        result = self.game.player_hit()
        self.player_label.config(text=f"Player: {self.game.player_hand}")
        if result:
            self.result_label.config(text=result)

    def dealer_turn(self):
        result = self.game.dealer_turn()
        self.dealer_label.config(text=f"Dealer: {self.game.dealer_hand}")
        self.result_label.config(text=result)

if __name__ == "__main__":
    game = Blackjack()
    GUI(game)