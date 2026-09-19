# Function

Anatomy of a function signature

1. Use a nice, meaningful name
This name gives the user of your function a good idea of what it does.  

2. List of parameters (optional)
A function can have no parameters or it can have one or more parameters.  
Parameters = they are part of the function definition  
Arguments = actual values passed while calling the function  

3. Starts with `def` and ends with `:`

---

Optional parameters

---

Returns a single result

A function can return multiple values seperated by comma but then it is automatically  
converted into a tuple and returned as a single tuple.

If a function tries to return more than one result, the  
collection of returned values are bundled together  
as a single tuple. This is due to the fact that Python  
functions only ever return a single result.  

Example: swimclub.py module file  

```python
import statistics

__all__ = ['read_swim_data']

# File location
FOLDER = "swimdata"

def _time_to_hundredths_seconds(time_str):
    parts = time_str.split(":")
    if len(parts) == 2:
        minutes, rest = parts
    else:
        minutes = 0
        rest = parts[0]

    parts = rest.split(".")
    if len(parts) == 2:
        seconds, hundredths = parts
    else:
        seconds = parts[0]
        hundredths = 0

    total_hundredths = (int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths)
    return total_hundredths

def _time_to_minutes_seconds_hundredths(time_value):
    mins_secs, hundredths = str(round(time_value / 100, 2)).split(".")
    mins_secs = int(mins_secs)
    mins = mins_secs // 60
    secs = mins_secs - (mins * 60)
    return f'{mins}:{secs}.{hundredths}'

def read_swim_data(filename):
    # Extracting data from the filename.
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")

    # Reading data from the file
    with open(f"{FOLDER}/{filename}") as file:
        lines = file.readlines()

    # We have only one line of data, getting time entries from it.
    times = lines[0].strip().split(",")

    time_values = []
    for t in times:
        value = _time_to_hundredths_seconds(t)
        time_values.append(value)

    average_time = _time_to_minutes_seconds_hundredths(statistics.mean(time_values))

    return swimmer, age, distance, stroke, times, average_time
```

Example: "swimclub" module usage

```python
import swimclub

result = swimclub.read_swim_data("Abi-10-50m-Back.txt")

print(result)
```

Here when we call `swimclub.read_swim_data` function, it returns a tuple with 6 values.  

---

Commenting/documenting functions

Use Docstrings to describe what a function does.  

Docstrings

* String (block of text) describing a function.
* Help users understand how to use a function.
* Docstring is displayed when we call `help()` function.
* `print(round.__doc__)` <-- programmatically accesing the Docstring.

Docstrings are crucial for documenting what a function does and how to use it.  
Docstrings are accessible using the `help()` function or by accessing the function's  
`__doc__` attribute, known as "dunder-doc".  

Here are the key points:  

* **Docstrings**: A block of text that describes what a function does, making it easier for others (and yourself) to understand your code.
* **Accessing Docstrings**: You can view a function's docstring by using `help(function_name)` or `function_name.__doc__`.
* **Creating Docstrings**: To add a docstring to a function, you use triple quotes ("""Docstring""") directly after the function's definition line. This can be a single-line docstring for simple functions or a multi-line docstring for more complex functions.
* **Multi-line Docstrings**: For detailed documentation, you include a summary line, a blank line, and then details about the function's arguments (Args:) and return value (Returns:), each on its own line and properly indented.

---

When to make a custom function?  

Considerations for making a custom function:  

* DRY (Don't Repeat Yourself), are you repeating the same code again and again?
* Number of lines
* Code complexity
* Frequency of usage

---

Positional Arguments  
Positional arguments are provided in order.  
Order of arguments is important.  

Keyword Arguments  
Keyword arguments are named explicitly in the function call, improving code readability.
Order of arguments is not important.  

Default Arguments  
We can set a default value for an argument.  

---

Arbitrary positional arguments  

Arbitrary positional arguments - converted to a tuple

- Docstrings help clarify how to use custom functions
- Arbitrary arguments allow functions to accept **any number** of arguments

```python
# Allow any number of positional, non-keyword arguments
def average(*args):
    # Function code remains the same
```

- Conventional naming: `*args`
- Allows a variety of uses while producing expected results!

Args create a single iterable  

- `*` : Convert arguments to a single iterable (tuple)

```python
# Calculating across multiple lists
print(average(*[15, 29], *[4, 13], *[11, 8]))
```

**Output:**  

```
13.33
```

---

Arbitrary keyword arguments  

Arbitrary keyword arguments - converted to a dictionary  

```python
# Use arbitrary keyword arguments
def average(**kwargs):
    average_value = sum(kwargs.values()) / len(kwargs.values())
    rounded_average = round(average_value, 2)
    return rounded_average
```

- Arbitrary keyword arguments: `**kwargs`
- `keyword=value`

Using arbitrary keyword arguments  

```python
# Calling average with six kwargs
print(average(a=15, b=29, c=4, d=13, e=11, f=8))
```

**Output:**  

```
13.33
```

```python
# Calling average with one kwarg
print(average(**{"a":15, "b":29, "c":4, "d":13, "e":11, "f":8}))
```

Each key-value pair in the dictionary is mapped to a keyword argument and value.  

**Output:**  

```
13.33
```

Kwargs create a single iterable

```python
# Calling average with three kwargs
print(average(**{"a":15, "b":29}, **{"c":4, "d":13}, **{"e":11, "f":8}))
```

**Output:**  

```
13.33
```

Arbitrary Positional Arguments:  
By prefixing a parameter with an asterisk `*`, you can pass any number of positional  
arguments to a function. These arguments are accessed within the function as a tuple.  
For example, defining a function `concat(*args)` enables it to concatenate any number  
of strings passed to it.

Arbitrary Keyword Arguments:  
Similarly, by using two asterisks `**` before a parameter, a function can accept any  
number of keyword arguments. Inside the function, these are treated as a dictionary,  
allowing for flexible data handling. Modifying the `concat` function to  
`concat(**kwargs)` lets it concatenate strings based on keyword arguments.
