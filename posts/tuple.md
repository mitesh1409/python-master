# Tuple

Python’s docs state that a tuple is an immutable sequence.  

It can sometimes help to think of a tuple as a constant list.  
Once values are assigned to a tuple, the tuple cannot change, it’s immutable.

As tuples are immutable, once defined, they cannot change.  
So a tuple always has a fixed number of slots.  

* Immutable - can't be changed
    - can't add values
    - can't remove values
    - can't change values

* Ordered just like lists and dictionaries
    - can access elements by index using square brackets `[]`
    - can subset by index i.e., [0]

* Useful for location information or identifiers

Tuples are great if we need to prevent information from being edited,  
ensuring data integrity, such as for location information or identifiers.  

Creating a tuple  
Use parentheses and provide values separated by commas.  

```python
card = ("King", "Diamond") # King of Diamond
```

We can use the built-in function `tuple()` to convert another data structure to a tuple.  
This is called casting to a tuple.

---

A single value tuple always ends with a comma to avoid ambiguity with any other type single value.

```python

type((55)) # int
type((55,)) # tuple

```
