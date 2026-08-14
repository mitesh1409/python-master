import random

# v2

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = list(range(2, 11))

# Populate the deck with all 52 cards.
deck = set()

for suit in suits:
    for card in faces + numbered:
        deck.add((card, suit))

print('Total Cards', len(deck))

print('\n')

print(deck)
print('\n')

cardDrawn = random.choice(list(deck))
print('Card Drawn', cardDrawn)
print('\n')

deck.remove(cardDrawn)
print('Cards Remaining', len(deck))
print('\n')

# Randomly draw a card from the deck and remove it from the deck.
def draw():
    if len(list(deck)) == 0:
        return None
    cardDrawn = random.choice(list(deck))
    deck.remove(cardDrawn)
    return cardDrawn

print('Card Drawn', draw())
print('\n')
print('Card Drawn', draw())
print('\n')
print('Card Drawn', draw())
print('\n')

card = ("King", "Hearts")
if card in deck:
    print('Card is in the deck')
else:
    print('Card is not in the deck')

print('\n')
