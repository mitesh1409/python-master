# Generators

```python
result = (num for num in range(6)) # This is a generator.

for num in result:
    print(num)

print(list(result))
```

---

## Generators > Lazy Evaluation

We can use `next()` to evaluate a generator, this is Lazy Evaluation.  
The evaluation of the expression is delayed until its value is needed.  

```python
result = (num for num in range(6))

print(next(result))

print(next(result))

print(next(result))
```

Where this is useful?  

Generators are very useful when working with extremely large sequences  
as you don't want to store the entire list in memory,  
but you want to generate elements of the sequence on the fly when required.  

Whereas List Comprehension will generate the entire list in memory,  
which is very memory intensive. Our application may run out memory as well.  

---

## Generators vs List Comprehensions

```python
googol_list = [num for num in range(10**100)] # Googol
```

Here we are trying to generate a list of numbers from 1 to Googol.  
This is very memory intensive, and there is a chance that our application may run out of memory.  

```python
googol_generator = (num for num in range(10**100)) # Googol
```

Here we get a generator object, it does not create the entire list.  
So Generators are memory efficient compared to List Comprehensions.  

> A list comprehension produces a list as output, a generator produces a generator object.

List Comprehensions  
Provides the whole list.  
If the list is huge/big then it will require more memory,  
and there is a chance that application may run out of memory  
because of this.  

Generators  
They provide the generator object.  
We can generate elements of the sequence on the fly when required.  
It can be used to stream data.  
Memory requirements stays low regardless of the amount of data processed  
by Generators.  

---

```python
import sys

one_million_list = [num for num in range(10*100000)]
one_million_generator = (num for num in range(10*100000))

print(f"List: {sys.getsizeof(one_million_list):,} bytes")
print(f"Generator: {sys.getsizeof(one_million_generator):,} bytes")
```

**Typical output (exact numbers vary by Python version):**
```
List: 8,448,728 bytes     # ~8 MB
Generator: 200 bytes      # tiny, and constant
```

---

**Heads-up on the numbers:** `sys.getsizeof()` on a list measures only the list container (the array of pointers), not the integer objects it points to. As we saw earlier with the list vs numpy comparison, the true list footprint is larger:

```python
list_total = sys.getsizeof(one_million_list) + sum(sys.getsizeof(n) for n in one_million_list)
print(f"List total: {list_total:,} bytes")  # ~36 MB
```

(Small integers from -5 to 256 are cached by Python, so the exact total is a little lower than a naive count, but it's still several times the container size.)

---

**Why the generator stays tiny:**

The generator object stores only its current state (where it is in the loop), not the values:

```python
small = (num for num in range(10))
big   = (num for num in range(10**9))

print(sys.getsizeof(small))  # same size
print(sys.getsizeof(big))    # same size, even for a billion values
```

---

**Trade-off to remember:**

| | List | Generator |
|---|---|---|
| Memory | Grows with size | Constant |
| Reuse | Iterate many times | **One pass only**, then exhausted |
| Indexing `x[5]` | Yes | No |
| `len()` | Yes | No |

```python
gen = (n for n in range(3))
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] since it is already consumed
```

---

> 💡 Use a generator when you only need to loop through values once (for example, summing or streaming a large file). Use a list when you need to reuse values, index them, or know the length. `sum(num for num in range(10**6))` works without ever building the million-item list.

---

## Generator Function

There are generator functions as well. Generator functions are functions that,  
like generator expressions, `yield` a series of values, instead of returning a  
single value. A generator function is defined as you do a regular function,  
but whenever it generates a value, it uses the keyword `yield` instead of `return`.

sequence.py

```python
def num_sequence(n):
    """
    Generate integer numbers from 0 to n.
    """

    num = 0
    while num < n:
        yield num
        num += 1
```

Using this generator function.  

```python
result = num_sequence(5)
print(type(result))
```

Output:  

```
<class 'generator'>
```

We get the generator object here.  
We can then iterate over this generator object to get the required values.  

```python
for item in result:
    print(item)
```

Output:  

```
0
1
2
3
4
```

---

If you have ever iterated over a dictionary with `.items()`,  
or used the `range()` function, for example, you have already  
encountered and used generators before, without knowing it!  
When you use these functions, Python creates generators for  
you behind the scenes.

---

* Generator expressions create generator objects with a syntax similar to list comprehensions but use parentheses () instead of square brackets []. These objects can generate items on the fly without storing the entire list in memory, making them more memory-efficient for large datasets.

* The concept of lazy evaluation, which means that the generator doesn't produce the elements until they are needed. This is particularly useful when dealing with very large data sequences.

* How to write generator functions using the yield keyword. Unlike regular functions that return a single value using return, generator functions yield a series of values, making them iterable.

* The practical differences between list comprehensions and generator expressions through examples. For instance, you saw how to create a list of members from a list fellowship with names longer than 7 characters using both methods, highlighting the memory efficiency of generators.
