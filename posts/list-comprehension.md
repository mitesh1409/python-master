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
