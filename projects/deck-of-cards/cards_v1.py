import random

# v1
# This is a simple approach to draw a card from a deck of 52 cards.
# Problem with this approach is that it does not keep track of the cards 
# that have already been drawn. So, it is possible to draw the same card multiple times.
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = list(range(2, 11))

def draw():
    the_suit = random.choice(suits)
    the_card = random.choice(faces + numbered)
    return the_card, the_suit

print("Cards v1")

print(draw())
print(draw())
print(draw())
