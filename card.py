class Card:
    CARD_VALUES={
        "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11
    }

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

    def get_value(self):
        return Card.CARD_VALUES[self.rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"
