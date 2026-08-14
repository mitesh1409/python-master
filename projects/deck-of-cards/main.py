import random

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = list(range(2, 11))

def draw():
    the_suit = random.choice(suits)
    the_card = random.choice(faces + numbered)
    return f'{the_card} from {the_suit}'

def main():
    print("Hello from deck-of-cards!")
    print(draw())
    print(draw())
    print(draw())

if __name__ == "__main__":
    main()
