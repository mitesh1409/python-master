# Python - Learning Topics

**Ideas**  

Idea is to create a blog post series or a handbook of all these topics.  

Series name: Pythonverse  
Generate logo with GenAI  

Make use of gifs, pictures, memes, charts, diagrams.  

Comic style.  

Showing conversation between two guys:  
Tony Stark - Python Master  
Peter Parker - Aspiring Python Developer  

Learning by doing - exercises and assignments  

Small size lessons - 10-15 mins videos, 5-10 mins reading  

Open source markdown handbook (contains notes, exercise/assignments etc.)

Automate required updates in the content (with Python updates) using Agentic AI in place.  
This will keep the content up to date with Python updates.  
Add change log to track updates.  

---

**Index**  


---

#1 Python Introduction

A brief history  
About the language - Swiss Army Knife  
Where it is used  
Popularity  
Ecosystem  
etc.

---

#2 Setup Python & Hello World :)  

Installation  
Professional project setup  
Code editor/IDE  
Jupyter notebook  
Interactive Python  
pip vs uv  
Your first Python program - Hello World :)  
etc.

---

#3 Variables  

How to declare variables  
Scope  
Life Cycle  
Naming conventions  
type()  
id()  
Can we provide type to variables (like in TypeScript)?  

---

#4 Data types  

String  
Number  
Boolean  
Type casting  

Data types in Python

- number = integer, float, complex
- boolean = True, False
- text = string
- sequence = list, tuple, range
- set = set
- mapping = dictionary
- Null type = <class 'NoneType'>

@todo  
Explore about number -> complex type.

Mutable vs Immutable Data types

Mutable = list, dictionary, set

Immutable = int, float, bool, str, tuple

---

Operators in Python

Arithmatic operators = `+`, `-`, `*`, `/`, `//`, `%`, `**`

Comparison operators = `>`, `>=`, `<`, `<=`, `==`, `!=`

Logical operators = `and`, `or`, `not`

Assignment operators = `=`, `+=`,...

Identity operators = `is`  
It checks references not values.

Membership operators = `in`, `not in`

Bitwise operators

How to get bit representation of a number?  
For example 7 = 111, 8 = 1000 etc.

Binary operators

---

In Python, assignment operators are used to assign values to variables. The most fundamental assignment operator is the single equal sign (=), which takes the value or expression on the right-hand side and assigns it to the variable on the left-hand side.
Python also features augmented assignment operators (compound operators), which perform a mathematical or bitwise operation on the variable and then assign the updated result back to that same variable.

## Core Python Assignment Operators

| Operator | Name | Example | Equivalent To |
|---|---|---|---|
| = | Assignment | x = 5 | x = 5 |
| += | Addition Assignment | x += 3 | x = x + 3 |
| -= | Subtraction Assignment | x -= 3 | x = x - 3 |
| *= | Multiplication Assignment | x *= 3 | x = x * 3 |
| /= | Division Assignment (always returns a float) | x /= 3 | x = x / 3 |
| %= | Modulus Assignment (remainder) | x %= 3 | x = x % 3 |
| //= | Floor Division Assignment | x //= 3 | x = x // 3 |
| **= | Exponentiation Assignment | x **= 3 | x = x ** 3 |

## Bitwise Assignment Operators

These are used for low-level operations on binary digits:

* &= (Bitwise AND): x &= 3 → x = x & 3
* |= (Bitwise OR): x |= 3 → x = x | 3
* ^= (Bitwise XOR): x ^= 3 → x = x ^ 3
* >>= (Right Shift): x >>= 3 → x = x >> 3
* <<= (Left Shift): x <<= 3 → x = x << 3

## Special Assignment Features in Python

## 1. The Walrus Operator (:=)
Introduced in Python 3.8, the walrus operator allows you to assign a value to a variable inside an expression (like an if statement or a while loop).

## Without walrus operator
n = len(my_list) if n > 10:
    print(f"List is too long: {n} elements")

## With walrus operator
if (n := len(my_list)) > 10:
    print(f"List is too long: {n} elements")

## 2. Multiple & Chained Assignment
Python allows you to assign a single value to multiple variables simultaneously, or unpack structures quickly:

## Chained assignment
x = y = z = 10

## Multiple assignment (Unpacking)
a, b = 1, 2  

## Easy variable swapping
a, b = b, a  

## Common Pitfall: = vs ==
Always remember that = is used to store data inside a variable. If you want to check if two values are equal, you must use the comparison operator ==. Python explicitly prevents you from accidentally using = inside conditional expressions like if x = 5: to keep your code safe.

---

#5 Math operators and "math" library functions

+, -, *, /, //, %, ** etc.
math.sqrt()
math.pi
math.floor()
math.ceil()
etc.

format()

---

#6 Strings

Strings are immutable in Python.

String functions.

---

#7 Lists

Lists are mutable

---

#8 If Condition

Simple if
if-else
if-else-if ladder

---

#9 Loops - for, while

for  
while  
continue  
break  

---

#10 Functions

documentation  
return type  
specifying types for the parameters and return value  
scope of variables defined inside a function  

---

#11 Dictionaries

Lists Vs Dictionaries  
Hash Map  

---

#12 Tuples

Lists Vs Tuples  
Tuples are immutable  

---

#13 File Handling

read  
write  
delete  
exception handling  
reading text file  
reading csv file  
using "with"  
how to read/write very large files  

---

#14 Modules  

Built-in - provided by Python  
3rd Party - installed by a developer for the application  
Custom - written by a developer for the application  

---

#15 pip, uv

pip Vs uv

install  
uninstall  
update  
etc.

To check the version of the installed module  
pip freeze | grep pandas  
pip freeze | grep numpy  
Explore what are the other ways to check this.

---

## PEP 8 Style Guide for Python Code

* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [PEP-8 Tutorial: Code Standards in Python](https://www.datacamp.com/tutorial/pep8-tutorial-python-code)

How to implement PEP 8 Styling in your codebase?
https://docs.astral.sh/ruff/

---

## OOP in Python

* Class
* Constructor
* Object
* Static/Non-static Methods (behaviour)
* Static/Non-static Properties (state)

---

## Decorators in Python

[Decorators in Python](./decorators.md)

---

## FastAPI

[FastAPI](./fastapi.md)
