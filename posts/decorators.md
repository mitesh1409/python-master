## Decorators in Python

A decorator is a function that **wraps another function to add extra behaviour** without modifying its original code.

---

## Without Decorator

Say you have multiple functions and you want to log how long each one takes:

```python
import time

def get_stocks():
    start = time.time()
    # actual function work
    print("Fetching stocks...")
    time.sleep(1)
    end = time.time()
    print(f"get_stocks took {end - start:.2f} seconds")

def get_news():
    start = time.time()
    # actual function work
    print("Fetching news...")
    time.sleep(2)
    end = time.time()
    print(f"get_news took {end - start:.2f} seconds")

get_stocks()
get_news()
```

**Problems:**
- Timing logic is **repeated** in every function
- Violates **DRY** (Don't Repeat Yourself) principle
- If you want to change the logging format, you must update every function

---

## With Decorator

```python
import time

# The decorator function
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # calls the original function
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

# Applying the decorator
@timer
def get_stocks():
    print("Fetching stocks...")
    time.sleep(1)

@timer
def get_news():
    print("Fetching news...")
    time.sleep(2)

get_stocks()
get_news()
```

**Output:**
```
Fetching stocks...
get_stocks took 1.00 seconds
Fetching news...
get_news took 2.00 seconds
```

---

## How it works step by step

```python
@timer
def get_stocks():
    ...

# ↑ This is just a shorthand for:
get_stocks = timer(get_stocks)
```

So when you call `get_stocks()`, you're actually calling `wrapper()` which:
1. Records start time
2. Calls the original `get_stocks()`
3. Records end time
4. Prints the duration

---

## Key Benefits

| Without Decorator | With Decorator |
|---|---|
| Timing logic repeated everywhere | Written once, applied anywhere |
| Hard to maintain | Change decorator = changes everywhere |
| Clutters the actual function | Function stays clean and focused |

---

> 💡 **Real world uses of decorators:**
> - `@timer` — performance monitoring
> - `@login_required` — authentication in web frameworks like Django
> - `@retry` — retry a function if it fails
> - `@cache` — cache results to avoid repeated computation
