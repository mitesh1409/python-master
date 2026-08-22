# dunder name & dunder main

Following if statement is a bit of a celebrity, as it appears at the bottom of almost all the Python applications.  

```python
if __name__ == "__main__":
```
It is an important Python programming idiom,  
as it lets you control what happens when your code is either  
(1) imported or  
(2) executed directly by the Python interpreter

Let’s explain what happens with the help of the world’s smallest Python module.

World’s smallest Python module -> whoami.py

```python
print(f"Hello, I am {__name__}.")
```

When this module runs, the current value of “dunder name” appears as part of  
this module’s friendly message.

When you run this module directly, it gives the below output:

```
Hello, I am __main__.
```

But when you import this module ("whoami") into any other module/file,  
it gives different output.

```
Hello, I am whoami.
```

When the module code is executed directly by the Python interpreter,  
__name__ is set to the value __main__ by default.

When the module code is imported by the Python interpreter, not directly executed,  
__name__ is set to the the name of the module being imported.

In Python, a file is treated as a module.  
And module name is same as the file name.  

> Note: the code in all modules is executed top-to-bottom when it is imported.
