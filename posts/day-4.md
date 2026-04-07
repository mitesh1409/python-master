# Day #4: Functions & Methods

What we will learn:  

1. What is a function?
2. How to get help on a function?
3. Type casting functions
4. Methods

#1  
What is a function?

A function is a piece of reusable code, that is responsible to do a particular task.

We have many built-in functions in Python, and if required we can write our own custom function as well.

Examples of some of the built-in functions in Python are:  

* `type()`
* `len()`
* `max()`
* `min()`
* `round()`
* `help()`
etc.

Built-in Functions:  
These are pre-defined functions in Python that you can use without writing your own code.

Imagine a function as a "Black Box" that takes input and produces output.  
Some magic happens inside that "Black Box", but as a consumer we don't need to worry about it.  

As a consumer we don't need to worry about how the function works internally,  
we just need to know about what input it needs and what will be the output,  
so that we can use the function correctly.


#2  
How to get help on a function?

You can check Python's documentation for a list of available built-in functions.  

Reference:  

[Python | Built-in Functions](https://docs.python.org/3/library/functions.html)

Or use `help()` function.

```python
help(max)

# OR

?max
```


#3  
Type casting functions

* `str()`
* `bool()`
* `int()`
* `float()`

`str()`  
Return a str version of object.

`bool()`
Return a Boolean value, i.e. one of True or False. 

`int()`
Return an integer object constructed from a number or a string, or return 0 if no arguments are given.

`float()`
Return a floating-point number constructed from a number or a string.


#3  
Methods

Everything in Python is an Object - means that all data — from simple numbers to complex functions  
and modules — is represented as an object in memory.

In Python, methods are indeed functions that are "associated" with an object or a class.  
While they look like regular functions, they are defined inside a class and are designed to define  
the behaviors and actions that an object of that class can perform.

Methods = Functions that belong to objects

list methods  

```python
fruits = ['Apple', 'Banana', 'Watermelon', 'Papaya', 'Grapes']

print(fruits.index('Papaya'))

print(fruits.count('Apple'))

fruits.append('Mango')

```

str methods  

```python

first_name = 'john'
last_name = 'wick'
full_name = first_name + ' ' + last_name

full_name.capitalize()

full_name.replace('john', 'peter')

```

* Everything = Object
* Different objects have different methods available
* Methods may or may not change the underlying object on which they are called



Object has one or more methods.

Optional input parameters

Type hinting input parameters and return value


## Summary

## Next -> Day #5: Packages
