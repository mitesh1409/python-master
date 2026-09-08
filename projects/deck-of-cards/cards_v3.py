import random

class CardDeck:
    def __init__(self):
        self.reset()

    def reset(self):
        suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
        faces = ["Jack", "Queen", "King", "Ace"]
        numbered = list(range(2, 11))
        self.deck = set()
        for suit in suits:
            for card in faces + numbered:
                self.deck.add((card, suit))

    def draw(self):
        if len(list(self.deck)) == 0:
            return None
        card = random.choice(list(self.deck))
        self.deck.remove(card)
        return card

    def __len__(self):
        return len(list(self.deck))
