# underscore - dummy variable

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

---

**Yes, using an underscore (`_`) as a dummy or throwaway variable is a standard, widely accepted convention in the Python community.**

Python's syntax sometimes requires a variable name even if you don't intend to use the value. The single underscore signals to both Python tools (like linters and IDEs) and human readers: *"A value goes here, but I am intentionally ignoring it."*

### Common Uses of `_` as a Dummy Variable

1. **In loops (when the index/value isn't needed):**
```python
for _ in range(5):
    print("Hello!")  # We don't care about the loop iteration number

```


2. **In sequence unpacking (ignoring specific items):**
```python
x, _, z = (10, 20, 30)  # We want the first and third items, but ignore the middle one

```


3. **In function overloading / dispatching (like your previous example):**
```python
@format_value.register
def _(value: str):  # The function name doesn't matter because it's registered under format_value
    return value.upper()

```


4. **As a wildcard in pattern matching (`match`/`case`):**
In modern Python (3.10+), `_` is an official built-in wildcard keyword in `match` statements to catch any remaining cases (like a `default` case).

> **Note on other meanings of `_`:** In the interactive Python REPL (terminal), `_` automatically stores the result of the last evaluated expression. It is also commonly imported as an alias for translation functions (`gettext`) in internationalization (i18n). Because of this, heavy localization codebases sometimes avoid using `_` as a dummy variable.

---

### Are there alternative ways or conventions for dummy variables?

Technically, Python doesn't have a unique, built-in "dummy keyword" (like some languages use `null` or a wildcard symbol exclusively for syntax). Any valid variable name will work. However, if you cannot or do not want to use a single underscore `_`, developers use a few other standard conventions:

#### 1. Descriptive Prefixes (`unused_` or `dummy_`)

If you want to make your code more readable or if your linter flags unused variables, you can prefix names with `unused_` or `dummy_`.

* *Example:* `for unused_index in range(5):` or `x, dummy_value, z = data`.
* Many popular linters (like Flake8 or Pylint) are explicitly configured to ignore unused variable warnings for any name starting with `unused_` or `dummy_`.

#### 2. Multiple Underscores (`__` or `___`)

If you are unpacking a tuple and need to ignore multiple separate items, you can actually repeat a single `_` (e.g., `x, _, _, y = data`), because Python just overwrites the `_` variable sequentially.
However, if you want distinct visual placeholders, some developers use double underscores (`__`) or triple underscores (`___`):

```python
x, __, ___, y = (1, 2, 3, 4)

```

#### 3. Numbered Underscores (`_1`, `_2`)

Similar to multiple underscores, some developers use `_1`, `_2`, etc., when unpacking complex structures where they want to distinguish between multiple ignored positions, though this is less common than standard `_`.
