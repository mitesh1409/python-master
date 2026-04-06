# Day #2: Variables & Data Types

What we will learn:  

1. Variables in Python
2. Data Types in Python


#1. 
Variables in Python  

What?

Why use variables?

How to declare?

How to name OR naming conventions?

Variables are labels they store references not the actual value.  

Example:  
Suppose we want to write a script to calculate BMI.  
BMI = weight in kg / square of height in meter  

```python
height = 1.79 # meters
weight = 68.7 # kilograms

bmi = weight / height ** 2
```

#2. 
Data Types in Python

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

## Summary


## Next -> Day #3: Python Lists
