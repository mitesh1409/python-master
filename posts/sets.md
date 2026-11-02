# Sets

Sets in Python  

* Contain unique data, can't have duplicates.
* Immutable/Unchangeable.
    * Can add/remove values, can't change them.
* Ideal to identify and remove duplicates.
* Quick to search (compared to other data structures such as lists).
* Don't have an index, can't use `[]` to subset.

We can convert a list to a set using `set()` built-in function.  
This process is called casting a list to a set.  

```python
# Existing list variable
ingredients_list = ["pasta", "tomatoes", "garlic", "basil",
                    "olive oil", "pasta", "salt", "garlic"]

# Convert to a set
unique_ingredients = set(ingredients_list)

# Check the data type
type(unique_ingredients) # <class 'set'>
```

Sorting a set  

To sort a set we can use built-in function `sorted()`, pass a set into it,  
it returns a list of sorted items.  
The original set remains unchanged.  

```python
ingredients = {"pasta", "tomatoes", "garlic", "basil",
               "olive oil", "pasta", "salt", "garlic"}

print(sorted(ingredients))
```

Also note that while defining a set if it contains duplicate values  
then it will remove duplicates automatically, no need to do anything extra.  

Creating a set  
Use curly braces and provide values separated by commas.  

```python
ingredients = {"pasta", "tomatoes", "garlic", "basil", "olive oil", "salt"}
```

We can use the built-in function `set()` to convert another data structure to a set.  
This is called casting to a set and while doing this duplicate values are removed  
automatically.  

---

How to create an empty set?

```python
# incorrect
empty_set = {}
print(type(empty_set))

# correct
empty_set = set()
print(type(empty_set))
```

---

set operations

union

intersection

difference

---

How can I access an element from a set?  

How can I loop through a set?  

Provide examples.

## Accessing elements of a set

**You can't access by index.** Sets are unordered, so `s[0]` doesn't work:

```python
strokes = {"Free", "Back", "Fly"}

strokes[0]  # ❌ TypeError: 'set' object is not subscriptable
```

What you *can* do is check whether an element exists:

```python
if "Free" in strokes:   # ✅ O(1) membership test
    print("Found!")
```

---

## Looping through a set

```python
strokes = {"Free", "Back", "Fly"}

for stroke in strokes:
    print(stroke)
# Output order is not guaranteed, e.g. Back, Free, Fly
```

**Sorted order (returns a list):**
```python
for stroke in sorted(strokes):
    print(stroke)
# Back, Fly, Free
```

**With a counter, using `enumerate()`:**
```python
for i, stroke in enumerate(sorted(strokes)):
    print(i, stroke)
# 0 Back
# 1 Fly
# 2 Free
```

---

## Getting a single element out

**Convert to a list first (if you need a position):**
```python
items = list(strokes)
print(items[0])  # works, but which element is "first" is arbitrary
```

**`pop()` removes and returns an arbitrary element:**
```python
item = strokes.pop()
print(item)     # some element
print(strokes)  # that element is gone
```

**Get one element without removing it:**
```python
first = next(iter(strokes))
```

---

## Common set operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b   # union        → {1, 2, 3, 4, 5}
a & b   # intersection → {3}
a - b   # difference   → {1, 2}
```

---

> 💡 **Key point:** the order in which a set is iterated is arbitrary and can differ between runs, so never rely on it. If you need a specific order, use `sorted(my_set)`. If you need to access items by position, a set is the wrong data structure, so use a list or tuple instead.
