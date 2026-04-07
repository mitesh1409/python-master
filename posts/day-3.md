# Day #3: Python Lists

What we will learn:  

1. Python Lists
2. Subsetting Lists
3. IndexError: list index out of range
4. List Manipulation

#1.  
Python Lists

Variables of data types - float, int, str, bool can store a single value only.  

As a Data Scientist we need to work with multiple data points or data values.  

Mixed Data Types:  
Lists can contain a mix of different data types, including strings, floats, and  
even other lists.

Lists of Lists:  
You can create lists that contain other lists, which is useful  
for structuring more complex data.


What?

A list is a way to give a single name to a collection of values.

* Name a collection of values
* Heterogeneous in nature, it can contain values of multiple types
* Can be nested, a list can contain another list, a list of lists
* Can contain advanced types, such as lists, dictionaries etc.

List is a powerful data structure that allows you to store and manipulate  
collections of values efficiently.

Why?

Storing Data:  
Instead of using separate variables for each data point, you can store  
related data in a single list.  
For example, to store the areas of different rooms in your house:  

```python
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
```


How?
List Creation:  
You can create a list using square brackets [] and store multiple data types within it.

Example

```python
fruits = ['Apple', 'Banana', 'Watermelon', 'Papaya', 'Grapes']
vegetables = ['Potato', 'Tomato', 'Onion', 'Cabbage']
dairy_items = ['Milk', 'Butter', 'Ghee', 'Cheese', 'Paneer']
stationery_items = ['Pen', 'Pencil', 'Eraser', 'Notebook']

# Nested list
grocery_items = [fruits, vegetables, dairy_items, stationery_items]

type(grocery_items)

# List with mixed items, heterogeneous list
random_list = [11, 'Lion', True, 9.99, [10, 20, 30]]

type(random_list)
```

#2.  
Subsetting Lists - accessing, slicing

Accessing elements from a list  

You can access individual element of a list using its index.  
`my_list[index]`  
Where index is zero based, starts with zero.  
Negative index gives elements from the end of the list.  
-1 index gives the last element.  

Python lists have zero based index, meaning indexing starts with zero.  

```python
fruits = ['Apple', 'Banana', 'Watermelon', 'Papaya', 'Grapes']

fruits[0]
fruits[1]
fruits[2]
fruits[-1]
fruits[-2]

fruits[2:5]
fruits[:2]
fruits[2:]
```

You can use negative index to get elements from the end of the list.  

Index -1 gives the last element.  

Slicing elements from a list  

You can slice a list by using `my_list[start:end]` syntax.  
Where "start" is included, "end" is excluded.  

You can omit either "start" or "end".  
`my_list[:end]` - returns all the elements starting with index = 0 to index = (end - 1)
`my_list[start:]` - returns all the elements starting with index = start to the end of the list

#3.  

IndexError: list index out of range

While accessing an element if you specify an index which is out of range then it  
will throw/raise an error - "IndexError: list index out of range".

#4.  
List Manipulation  

Change list elements

```python
fruits = ['Apple', 'Banana', 'Watermelon', 'Papaya', 'Grapes']

# Change an element
fruits[0] = 'Mango'

# Changing all elements in the slice
fruits[1:4] = ['Orange', 'Sapodilla', 'Strawberry']
```

Add list elements

```python
fruits = ['Apple', 'Banana', 'Watermelon', 'Papaya', 'Grapes']

# Add 3 new elements by adding a list
fruits_new = fruits + ['Orange', 'Sapodilla', 'Strawberry']

# To add elements into the original array we can use append or insert methods.
fruits.append('Mango')

fruits.insert(5, 'Mango')
```

Remove list elements

```python
fruits = ['Apple', 'Banana', 'Watermelon', 'Papaya', 'Grapes']

# Removes an element at index 3
del fruits[3]
```

#5.  
How lists are stored?

Lists are stored inside the computer memory and a list variable stores a reference/address  
of this list's memory location.

```python
x = ["a", "b", "c"]

y = x

y[1] = "z"

print(y) # ["a", "z", "c"]
print(x) # ["a", "z", "c"]
```

Here when we assigned `x` to `y`, `y` got the same reference to the list that `x` is holding.  
This means both `x` and `y` have reference to the same list in the memory.  

```python
x = [1, 2, 3]

y = list(x)

y = x[:]
```


## Summary

* Python lists are used to store multiple data points under one variable.
* Lists can contain different data types, like numbers, strings, and even other lists.
* You create a list using square brackets, for example: [1, 2, 3].
* Lists are useful for organizing related data, such as family members' heights and names.
* Lists within lists (nested lists) allow for more complex data structures.
* Python provides tools to manipulate and access list elements easily.
* You access individual elements using their index, starting from 0.
* Negative indexes count from the end of the list.
* Slicing allows you to select multiple elements by specifying a range with a colon.
* The start index in slicing is included, but the end index is excluded.
* You can omit the start or end index to slice from the beginning or to the end of the list.
* IndexError: list index out of range

Subsetting lists in Python is essential for accessing and manipulating specific elements  
within a list.

Indexing: You accessed elements in a list using their index. For example, my_list[3] retrieves the fourth element.

Negative Indexing: You used negative indexes to count backward from the end of the list. For example, my_list[-1] retrieves the last element.

Slicing: You selected multiple elements by specifying a range. For example, my_list[1:4] retrieves elements from index 1 to 3.

You can change list elements using square brackets and assignment, e.g., my_list[7] = 1.86.

You can add elements to a list by concatenating with +, e.g., my_list + [10, 20, 30].

To remove elements, use the del command, e.g., del my_list[2].

Lists are stored in memory as references, so copying a list with = creates a shared reference.
To copy a list properly, use list(x) or slicing x[:] to create a new list in memory.


## Next -> Day #4: Functions
