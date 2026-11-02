# Data Types

* String
* Number
    - Integer (for whole numbers)
    - Float (numbers with decimal part)
    - Decimal
* Boolean

Boolean type supports only two values - `True` & `False`.  
These values are never quoted.  

Use built-in `type()` function to get the type of a variable in Python.  

---

Built-in Numeric Types

* Integer
    - whole numbers
* Float
    - contains fractional amount
    - can use scientific notation
* Decimal
    - exact precision
    - currency operations

```python
from decimal import Decimal
Decimal('123456789123456789')

int(123456789123456789)

float(123456789123456789)
```

---

Falsey Values

* `False`
* None
* `''` or `""`
* 0
* `set()`
* `{}`
* `[]`

```python
def isFalsey(value):
    return not bool(value)

falsey_values = [False, None, 0, '', "", [], set(), {}]

for value in falsey_values:
    print(f"Value: <{value}> | Is Falsey? {isFalsey(value)}")
```

```python
falsey_values = [
    False, None,
    0,               # int zero
    0.0,             # float zero
    0j,              # complex zero
    '', "",          # empty string
    [], (), {}, set(),   # empty list, tuple, dict, set
    range(0),        # empty range
    b'',             # empty bytes
    bytearray(),     # empty bytearray
]
```

Note that `''` and `""` are the same value in Python, so you only need one of them.

**Other falsey values worth knowing:**

```python
from decimal import Decimal
from fractions import Fraction

Decimal(0)      # falsey
Fraction(0)     # falsey
```

Other empty collections like `frozenset()`, `collections.deque()` and an empty `dict.keys()` view are falsey too.

---

**Custom objects:** a class is falsey if it defines `__bool__` returning `False`, or `__len__` returning `0`:

```python
class Basket:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

print(bool(Basket()))  # False, because __len__ returns 0
```

---

**General rule:** everything is truthy except `None`, `False`, zero of any numeric type, and empty sequences or collections.

---

> 💡 **Common gotchas:** these are all truthy, even though they look "empty":
> ```python
> bool("0")      # True, non-empty string
> bool("False")  # True, non-empty string
> bool([0])      # True, list has one element
> bool([[]])     # True, list containing an empty list
> ```
