# Datacamp - Introduction to Python

**Index**  

Getting Started  
1. Introduction to Python
2. Install Python & Professional Development Environment Setup
3. Your first Python program - Hello World!
4. How we can run/execute Python code?
5. Comments in Python
Variables and Types
6. Variables in Python
7. Data Types in Python

## Getting started with Python

### #1 Introduction to Python

Creator of Python  

High level programming language  

Interpreted, not compiled  

Synchronous or Asynchronous?  

How old Python is?  

What you can do with Python?  

Backed by whom? Sponsors?  
https://www.python.org/psf/sponsors/

Python is a versatile, open-source programming language created by Guido Van Rossum.  
It's widely used for various applications, including data science.

People often refer to Python as the "Swiss Army Knife" of programming languages  
as you can do almost anything with it.

### #2 Install Python & Professional Development Environment Setup

Python installation in Mac, Windows, Linux  

Setup Python without disturbing the system Python  

pip, pyenv Vs uv  

Professional Project Setup (industry standard)  

Set up Interactive Python via installing "ipykernel" package.  

Jupyter Notebook Setup  

Recommended IDEs - VS Code, PyCharm  

### #3 Your first Python program - Hello World!

Python scripts are text files with a .py extension.  

Write your first Python program - print Hello World!

### #4 How we can run/execute Python code?

There are multiple ways to execute Python code:  

* Interactive Shell/Python Shell from the terminal
* Interactive Python using "ipykernel" package
* Jupyter Notebook
* As a script

### #5 Comments in Python

Purpose of comments  
Single line  
Multi-line  

### #6 Variables in Python

What?

Why use variables?

How to declare?

How to name OR naming conventions?

Variables are labels they store references not the actual value.  

Variable scope

`id()` function

Example:  
Suppose we want to write a script to calculate BMI.  
BMI = weight in kg / square of height in meter  

```python
height = 1.79 # meters
weight = 68.7 # kilograms

bmi = weight / height ** 2
```

### #7 Data Types in Python

Data types in Python  

`type()` function

Type casting  

We can get the type of a variable using `type()` function.  

Type Checking: You can use the type() function to check the data type of a variable, e.g., type(bmi) returns float.

Primitive data types in Python are:  

* Integers (int): Whole numbers, e.g., savings = 100.
* Floats (float): Numbers with fractional parts OR Real numbers, e.g., half = 0.5.
* Strings (str): Text values, e.g., intro = "Hello! How are you?".
* Booleans (bool): Logical values, True or False, e.g., is_good = True.

Different data types = different behaviour!  

```python
print(2 + 3) # 5

print('Hello' + ' ' + 'Python') # Hello Python
```

How the code behaves depends on the data types.  

**Basic types:**

```python
x = 10          # int
y = 3.14        # float
name = "Mitesh" # str
is_active = True  # bool (True or False)
nothing = None  # NoneType
```

**Check the type:**

```python
type(x)      # <class 'int'>
type(name)   # <class 'str'>
```

**Collection types:**

```python
my_list   = [1, 2, 3]         # list   — ordered, mutable
my_tuple  = (1, 2, 3)         # tuple  — ordered, immutable
my_set    = {1, 2, 3}         # set    — unordered, no duplicates
my_dict   = {"name": "Mitesh"} # dict  — key-value pairs
```

**Type Casting**

```python
int("42")       # str  → int   : 42
float("3.14")   # str  → float : 3.14
str(100)        # int  → str   : "100"
bool(0)         # int  → bool  : False
bool(1)         # int  → bool  : True
list((1, 2, 3)) # tuple → list : [1, 2, 3]
```

**Truthy / Falsy — good to know:**

```python
bool(0)     # False
bool("")    # False
bool(None)  # False
bool([])    # False

bool(1)     # True
bool("hi")  # True
bool([1,2]) # True
```

> 💡 Any empty or zero value is `False`. Everything else is `True`.
