class Card:
    VALUES={
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11 
    }
    def __int__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        return self.VALUES[self.rank]

    def __str__(self):
        return self.rank + self.suit