# List Comprehension

Python list comprehension is a short, single-line way to create a new list  
from an existing list or iterable. It replaces long for loops, making your  
code cleaner, shorter, and often faster to run.

Every list comprehension lives inside square brackets `[]`  
and follows this basic recipe:

```
new_list = [expression for item in iterable if condition]

OR

[ output expression for iterator variable in iterable if predicate expression ]
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

---

## Nested Loops

```python
pairs = []

for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs.append((num1, num2))

print(pairs)
```

Do the same with list comprehension.  

```python
pairs = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
```

---

## List comprehension over iterables

You know that list comprehensions can be built over iterables. Given the following objects below, which of these can we build list comprehensions over?

```python
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

range(50)

underwood = 'After all, we are nothing more or less than what we choose to reveal.'

jean = '24601'

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

valjean = 24601
```

You can build list comprehensions over all the objects except the integer object `valjean`.

---

## Nested list comprehensions

Great! At this point, you have a good grasp of the basic syntax of list comprehensions. Let's push your code-writing skills a little further. In this exercise, you will be writing a list comprehension within another list comprehension, or nested list comprehensions. It sounds a little tricky, but you can do it!

Let's step aside for a while from strings. One of the ways in which lists can be used are in representing multi-dimension objects such as matrices. Matrices can be represented as a list of lists in Python. For example a 5 x 5 matrix with values 0 to 4 in each row can be written as:

```python
matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
```

Your task is to recreate this matrix by using nested listed comprehensions. Recall that you can create one of the rows of the matrix with a single list comprehension. To create the list of lists, you simply have to supply the list comprehension as the output expression of the overall list comprehension:

`[[output expression] for iterator variable in iterable]`

Note that here, the output expression is itself a list comprehension.

Solution:  

```python
matrix = [[num for num in range(0, 5)] for row in range(0, 5)]
```

**Nested List Comprehensions**: These allow for the creation of multi-dimensional lists. For example, generating a 5x5 matrix can be achieved with `[[col for col in range(5)] for row in range(5)]`.
