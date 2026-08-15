# Multiple assignment (aka unpacking)

Although the concept is not unique to Python, the notion of multiple assignment is a
powerful feature of the language.  

Also known as **unpacking** (within the Python world), this feature lets you assign to
more than one variable on the left of an assignment operator with a matching number
of data values on the right of the assignment operator.  

Example:  

```python

pie, meaning = 3.14, 42

```

Note the following: you can match any number of variable names against values
(as long as the number of each on both sides of the assignment operator
match). Python treats the data values on the right as if they are list-like, but
does not require you to enclose your lists (in this case) within square brackets.

Just make sure the number of data values
on the right match the number of variable
names on the left.

Python programmers describe the list as being
“unpacked” prior to the assignment, which is
their way of saying the list’s data values are
taken one-by-one and assigned to the variable
names one-by-one. The single list is unpacked
and its values are assigned to multiple variable
names, one at a time.

Reference:  
Book: Head First Python 3rd Edition
