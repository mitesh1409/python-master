# Functions

Functions contain a set of instructions to do a specific job/task.  
They are reusable piece of code.  

When to write a function?

* job/task is complex
* job/task is repetitive

There are two types of functions:  

#1 Built-in Functions
Provided by Python out of the box.
They are ready-to-use.

#2 Custom Functions
They are written by developer for the application.

---

## Built-in Python Functions

* `print()`
* `type()`
* `range()`
* `len()`
* `max()`
* `min()`
* `sum()`
* `round()`
* `sorted()`
* `zip()`
* `input()`
* `reduce()`
* `filter()`
* `any()`
* `all()`
* `map()`
* `enumerate()`

---

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

Best practice for default arguments

One of your co-workers (who obviously didn't take this course) has written this function for adding a column to a pandas DataFrame. Unfortunately, they used a mutable variable as a default argument value! Please show them a better way to do this so that they don't get unexpected behavior.

```python
def add_column(values, df=pandas.DataFrame()):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  df['col_{}'.format(len(df.columns))] = values
  return df
```

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

```python
def foo(*args):
    print(args, type(args))

foo(1, 2, 3, 4, 5)

def bar(**kwargs):
    print(kwargs, type(kwargs))

bar(greetings='Hello', name='Mitesh')
```

---

Create/build a tooltip for a given function.

```python
import inspect

def build_tooltip(function):
  """Create a tooltip for any function that shows the
  function's docstring.

  Args:
    function (callable): The function we want a tooltip for.

  Returns:
    str
  """
  # Get the docstring for the "function" argument by using inspect
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
```

---

Write functions to calculate mean and median.  

```python
def mean(values):
  """Get the mean of a list of values.

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float: A mean value.
  """
  mean = sum(values) / len(values)
  return mean

def median(values):
  """Get the mean of a list of values.

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float: A median value.
  """
  values = sorted(values)
  midpoint = int(len(values) / 2)

  if len(values) %2 == 0:
    median = (values[midpoint-1] + values[midpoint]) / 2
  else:
    median = values[midpoint]

  return median
```

---

When functions are called and arguments are passed,  
a reference is passed not the value.

```python
# Example #1
def border():
    print("=" * 40)

def add_to_list(a_list):
    print(f"add_to_list, id = {id(a_list)}")
    a_list.append(10)

def update_list(a_list):
    print(f"update_list, id = {id(a_list)}")
    a_list[0] = 99

some_list = [1, 2, 3]

print(f"module, id = {id(some_list)}")

print(some_list)
border()

add_to_list(some_list)

print(some_list)
border()

update_list(some_list)

print(some_list)
border()


# Example #2
def border():
    print("=" * 40)

def add_ten(value):
    print(f"add_ten - before addition, id = {id(value)}")
    value += 10
    print(f"add_ten - after addition, id = {id(value)}")

num = 5

print(f"module, id = {id(num)}")
print(num)
border()

add_ten(num)
border()

print(f"module, id = {id(num)}")
print(num)
border()
```

---

Function is also an object.

Function can have local variables or attributes.

```python
def foo():
    score = 0
    foo.team = 'India'
    return score + 99

print(foo())

print(dir(foo))

print(foo.team)

# print(score) # NameError: name 'score' is not defined

# print(foo.score) # AttributeError: 'function' object has no attribute 'score'
```

The core idea is right: a function is an object, and you can attach attributes to it. But there are a few issues in the notes.

---

**1. "Local variables or attributes" mixes two different things**

```python
def foo():
    score = 0          # local variable: lives only during the call
    foo.team = 'India' # function attribute: lives on the function object
    return score + 99
```

| | Local variable (`score`) | Function attribute (`foo.team`) |
|---|---|---|
| Lives in | The call's stack frame | The function object's `__dict__` |
| Lifetime | Gone when the call ends | Persists as long as `foo` exists |
| Accessible outside | No | Yes, as `foo.team` |

That is exactly why your two commented lines fail: `score` is not in global scope (`NameError`), and it was never attached to the function (`AttributeError`).

---

**2. Timing gotcha: `foo.team` doesn't exist until `foo()` runs**

The attribute is created inside the body, so it only appears after the first call:

```python
def foo():
    foo.team = 'India'
    return 99

print(foo.team)   # AttributeError: foo hasn't been called yet
foo()
print(foo.team)   # India
```

Your notes work only because `print(foo())` runs before `print(foo.team)`.

---

**3. The usual way: set attributes outside the function**

```python
def foo():
    return 99

foo.team = 'India'    # set once, at definition time
print(foo.team)       # works without calling foo()
```

---

**4. Practical use: state that survives between calls**

```python
def hit():
    hit.count += 1
    return hit.count

hit.count = 0

hit()
hit()
print(hit.count)   # 2
```

This is also how decorators often attach metadata (`wrapper.calls = 0`).

---

**5. Handy things to add to the notes**

```python
print(foo.__dict__)   # {'team': 'India'}: attributes live here
print(foo.__name__)   # 'foo'
print(type(foo))      # <class 'function'>
```

Functions can also be assigned to variables, passed as arguments, and returned from other functions. That is what "first-class objects" means, and it underpins closures and decorators.

---

**Suggested rewrite of the heading line:**

> A function is an object. It can have **attributes** (stored in `func.__dict__`), which are separate from its **local variables** (which exist only during a call).

> 💡 `print(dir(foo))` works, but the output is long and mostly dunder methods. `foo.__dict__` shows just your custom attributes, which is usually what you want to demonstrate.
