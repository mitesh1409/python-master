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

Commenting functions
