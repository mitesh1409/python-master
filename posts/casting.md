# Casting

## Type Casting Functions in Python

* `str()` - casts to string
* `int()` - casts to integer
* `float()` - casts to floating-point number
* `bool()` - casts to boolean
* `complex()` - casts to complex number
* `list()` - casts to list
* `tuple()` - casts to tuple
* `set()` - casts to set
* `frozenset()` - casts to immutable set
* `dict()` - casts to dictionary
* `bytes()` - casts to bytes
* `bytearray()` - casts to mutable bytearray

---

**Examples:**

```python
float("3.14")            # 3.14
bool(0)                  # False
complex(2, 3)            # (2+3j)

list("abc")              # ['a', 'b', 'c']
tuple([1, 2, 3])         # (1, 2, 3)
set([1, 2, 2, 3])        # {1, 2, 3}  (duplicates removed)
frozenset([1, 2, 3])     # frozenset({1, 2, 3})

dict([("a", 1), ("b", 2)])   # {'a': 1, 'b': 2}

bytes("hi", "utf-8")     # b'hi'
bytearray(b"hi")         # bytearray(b'hi')
```

---

**Related conversion functions** (also handy to include in your notes):

```python
chr(65)        # 'A'     int -> character
ord("A")       # 65      character -> int
bin(10)        # '0b1010'  int -> binary string
oct(10)        # '0o12'    int -> octal string
hex(255)       # '0xff'    int -> hex string
int("1010", 2) # 10      binary string -> int (base 2)
repr(obj)      # string representation meant for developers
```

---

**Things to note:**

- Casting can fail: `int("abc")` raises `ValueError`, and `int("3.14")` also raises `ValueError`. Use `int(float("3.14"))` instead.
- `int(3.9)` truncates toward zero and gives `3` (no rounding). Use `round()` for rounding.
- `dict()` needs key-value pairs, so `dict([1, 2, 3])` fails.
- Technically these are **constructors of built-in classes**, not "casting" in the C/Java sense. Python creates a new object of that type rather than reinterpreting the existing one. "Type conversion" is the more accurate term.

> 💡 **Quick memory aid:** casting functions are named exactly like the type they produce: `str`, `int`, `float`, `bool`, `list`, `tuple`, `set`, `dict`.
