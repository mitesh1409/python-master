# underscore in for loop

```python
import random

suits = ["Clubs", "Spades", "Hearts", "Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = list(range(2, 11))

def draw():
    the_suit = random.choice(suits)
    the_card = random.choice(faces + numbered)
    return f'{the_card} from {the_suit}'

for _ in range(5):
    print(draw())

```

**That’s Python’s default variable.**  

It’s typical for most loops to have a loop variable
associated with them (with “i” being a particular
favorite name among many programmers). However,
if your loop’s code doesn’t use that variable’s value,
Python lets you use the underscore character instead.

When you see the underscore in code, think “Ah ha!
A variable is syntactically required here, but it’s value isn’t
used, so the variable hasn’t been named.”

Reference:  
Book: Head First Python 3rd Edition
