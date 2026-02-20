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
    def format_hand(self, hand):
        return "[" + ", ".join(str(card) for card in hand) + "]"

    def display_hands(self, hide_dealer=True):
        print("\nDEALER's Cards:", end=" ")

        if hide_dealer:
            print(f"[{self.dealer_hand[0]}, ?]")
        else:
            dealer_total = self.calculate_total(self.dealer_hand)
            print(f"{self.format_hand(self.dealer_hand)} = {dealer_total}")

        player_total = self.calculate_total(self.player_hand)
        print(f"PLAYER's Cards: {self.format_hand(self.player_hand)} = {player_total}")

    def player_turn(self):
        while True:
            total = self.calculate_total(self.player_hand)

            if total > 21:
                print("🤯 OMG!!!!PLAYER IS BUST!!!!")
                break

            choice = input(" What you wanna do next? 🤔 Please type (h) for Hit/ (s) for Stand? ").strip().lower()

            if choice == "h":
                self.deal_card(self.player_hand)
                self.display_hands(True)

            elif choice == "s":
                break

            else:
                print("🫢 OOPS!! Invalid input. Please only type h or s. Strictly no other inputs..")

    def dealer_turn(self):
        print("\nDealer reveals cards...")
        while self.calculate_total(self.dealer_hand) < 17:
            self.deal_card(self.dealer_hand)

    def update_bankroll(self):
        player_total = self.calculate_total(self.player_hand)
        dealer_total = self.calculate_total(self.dealer_hand)

        if player_total > 21:
            self.bankroll -= Game.BET
            print("player lose 50")

        elif dealer_total > 21:
            self.bankroll += Game.BET
            print("player win 50")

        elif player_total > dealer_total:
            self.bankroll += Game.BET
            print("player win 50")

        else:
            self.bankroll -= Game.BET
            print("player lose 50")

        if self.bankroll < 0:
            self.bankroll = 0

        print(f"New Bankroll: ${self.bankroll}")

    def play_round(self):
        if self.bankroll < Game.BET:
            print("\ngame over")
            print(f"Final Bankroll: ${self.bankroll}")
            return False

        self.round_number += 1

        print(f"Bankroll: ${self.bankroll}")
        print(f"Round {self.round_number} ===")
        print(f"Bet: ${Game.BET}")

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
