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
