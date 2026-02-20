import random
from card import Card

class Game:
    BET = 50
    STARTING_BANKROLL = 1000

    def __init__(self):
        self.bankroll = Game.STARTING_BANKROLL
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.round_number = 0

    def create_deck(self):
        ranks = ["2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♠", "♥", "♦", "♣"]

        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

        random.shuffle(self.deck)

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)

    def calculate_total(self, hand):
        total = 0
        aces = 0

        for card in hand:
            total += card.get_value()
            if card.rank == "A":
                aces += 1

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def display_hands(self, hide_dealer=True):
        print("\nDEALER:", end=" ")

        if hide_dealer:
            print(f"[{self.dealer_hand[0]}, ?]")
        else:
            dealer_total = self.calculate_total(self.dealer_hand)
            print(f"{self.dealer_hand} = {dealer_total}")

        player_total = self.calculate_total(self.player_hand)
        print(f"PLAYER: {self.player_hand} = {player_total}")

    def player_turn(self):
        while True:
            total = self.calculate_total(self.player_hand)

            if total > 21:
                print("OMG!!!!PLAYER IS BUST!!!!")
                break

            choice = input(" What you wanna do next? 🤔 Please type (h) for Hit/(s) for Stand? ").strip().lower()

            if choice == "h":
                self.deal_card(self.player_hand)
                self.display_hands(True)

            elif choice == "s":
                break

            else:
                print("🫢 OOPS!! Invalid input. Please only type h or s. Strictly no other inputs..")

    def dealer_turn(self):
        print("\nDealer reveals his/her cards:")
        while self.calculate_total(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand)

    def update_bankroll(self):
        player_total = self.calculate_total(self.player_hand)
        dealer_total = self.calculate_total(self.dealer_hand)

        if player_total > 21:
            self.bankroll -= Game.BET
            print("**PLAYER LOSES!** -$50")

        elif dealer_total > 21:
            self.bankroll += Game.BET
            print("**PLAYER WINS!** +$50")

        elif player_total > dealer_total:
            self.bankroll += Game.BET
            print("**PLAYER WINS!** +$50")

        else:
            self.bankroll -= Game.BET
            print("**PLAYER LOSES!** -$50")

        if self.bankroll < 0:
            self.bankroll = 0

        print(f"New Bankroll: ${self.bankroll}")

    def play_round(self):
        if self.bankroll < Game.BET:
            print("\nGAME OVER - You're broke!")
            print(f"Final Bankroll: ${self.bankroll}")
            return False

        self.round_number += 1

        print("\n==============================")
        print("BLACKJACK")
        print(f"Bankroll: ${self.bankroll}")
        print(f"=== ROUND {self.round_number} ===")
        print(f"BET: ${Game.BET}")

        self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)
        self.deal_card(self.player_hand)
        self.deal_card(self.dealer_hand)

        self.display_hands(True)

        self.player_turn()

        if self.calculate_total(self.player_hand) <= 21:
            self.dealer_turn()
            self.display_hands(False)

        self.update_bankroll()
        return True
