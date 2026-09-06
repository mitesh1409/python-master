# Module

Once you move code into its own file,  
it becomes is a Python module,  
which you can import as needed.

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


This is a fully qualified name.  

When you refer to your function with  
“module DOT function,” you are  
qualifying the name of your function  
with the name of the module that  
contains it.  

As importing can sometimes be computationally expensive,  
a decision was made to cache imported modules.  

So when you import the same module multiple times in your code,  
during the first import module is loaded and cached,  
subsequent imports use the cached module.  
Even if the module is updated after the first import it still uses cached version,  
that is why module changes will not be reflected in your code.  

To solve this problem you need to restart your Python session,  
this will reset your Python cache.  

What’s the best way to restart my session?  

With Jupyter Notebook, there’s a big shiny  
Restart button at the top of the VS Code window that  
will do the trick. When you click on that, your previous  
Python session is deleted including its cache, and you  
get to start over.  

---

**Purpose of __all__:**  

It controls what gets exported when someone does `from module import *` — it defines the public API of your module.  

```python
__all__ = ['function1', 'function2']  # only these are exported

def function1():  # ✅ public
    ...

def function2():  # ✅ public
    ...

def _function3():  # ✅ private by convention
    ...

def _function4():  # ✅ private by convention
    ...
```

---

**Is it mandatory?**

No, it's completely optional. Without `__all__`:
- `from module import *` imports **everything** that doesn't start with `_`
- Explicit imports like `from module import function1` always work regardless

---

**Is it good to have?**

It depends on the size and purpose of your module:

| Scenario | Use `__all__`? |
|---|---|
| Small personal script | ❌ Not needed |
| Module used by others | ✅ Good practice |
| Library or package | ✅ Recommended |

---

> 💡 **Best practice combination** — use both `__all__` and `_` prefix together:
> - `_` prefix → signals private to IDEs and developers
> - `__all__` → enforces public API for `import *`

> 💡 Simple rule:
> - Script that runs on its own → __all__ not needed
> - Module that others import from → __all__ is good practice
