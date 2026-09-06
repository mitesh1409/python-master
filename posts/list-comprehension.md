# List Comprehension

Python list comprehension is a short, single-line way to create a new list  
from an existing list or iterable. It replaces long for loops, making your  
code cleaner, shorter, and often faster to run.

Every list comprehension lives inside square brackets `[]`  
and follows this basic recipe:

```python
new_list = [expression for item in iterable if condition]
```

**expression**: What you want to do to the item (the final result).  

**item**: The current element you are looking at.  

**iterable**: The original collection (like a list or a range of numbers).  

**if condition (Optional)**: A filter to only keep certain items.  


**Why List Comprehensions?**

Firstly, as well as requiring less code (which means  
comprehensions are easier on your fingers), the Python  
interpreter is optimized to run comprehensions as  
quickly as possible. This means comprehensions execute  
faster than the equivalent for loop code.

Secondly, comprehensions can be used in places where  
for loops can’t. Comprehensions can appear to the  
right of the assignment operator, which is something a  
regular for loop can’t do. This can be really powerful.

---

Comprehensions are typically one of two types:  
**transformational** and **filtering**.

* Transformational comprehensions (also called mappings) convert the values in one list to a new list of converted values.

* Filtering comprehensions are easy to spot: they have an if condition that must hold in order for a value to be appended to a target list.

* It’s perfectly acceptable to have a compehension that is both transformational and filtering (although we’re not sure what to call a list comprehension that does double-duty like this… mapfilter, maybe?).

---

Comprehension can be done with lists, dictionaries, sets and tuples.

**List Comprehension:**
```python
# Squares of numbers 1 to 5
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

---

**Dictionary Comprehension:**
```python
# Word and its length
words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'apple': 5, 'banana': 6, 'cherry': 6}
```

---

**Set Comprehension:**
```python
# Unique squares (duplicates removed automatically)
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # {1, 4, 9, 16}
```

---

**Tuple — small correction:**

Comprehension doesn't directly create a tuple. This creates a **generator**, not a tuple:
```python
gen = (x ** 2 for x in range(1, 6))
print(type(gen))  # <class 'generator'>
```

To get a tuple, wrap it with `tuple()`:
```python
squares = tuple(x ** 2 for x in range(1, 6))
print(squares)  # (1, 4, 9, 16, 25)
print(type(squares))  # <class 'tuple'>
```

---

**With filter condition — works the same way for all types:**
```python
# Only even numbers
evens_list = [x for x in range(10) if x % 2 == 0]
evens_dict = {x: x ** 2 for x in range(10) if x % 2 == 0}
evens_set  = {x for x in range(10) if x % 2 == 0}
```

---

> 💡 **The note about tuples** — technically Python has no tuple comprehension syntax. `(x for x in ...)` is a **generator expression**, not a tuple comprehension. It's a common misconception worth knowing.
