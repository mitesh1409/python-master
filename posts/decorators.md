# Decorators in Python

A decorator is a function that **wraps another function to add extra behaviour** without modifying its original code.

Decorator = Accessory  
Like an Accessory, a Decorator provides additional functionality, and can be reused  
wherever required without repeating the code.

Decorator helps to implement DRY principle.  

---

## Anatomy of a decorator function in Python

```python

# A decorator function takes actual function as an argument.
# It defines and returns a wrapper function.
def a_decorator(func):
    # It is called wrapper function, because it wraps actual function.
    # It contains decoration logic.
    def wrapper(*args, **kwargs):
        # Things that the decorator will do goes here.

        # Call the actual function and return results.
        result = func(*args, **kwargs)
        return result

    # Decorator returns a wrapper.
    return wrapper

# Decorator syntax, syntactic sugar
@a_decorator
def foo(one, two):
    return (one, two)

# This is same as the below code.
# This is what happens under the hood.
foo = a_decorator(foo)

# And then we call decorated function.
foo(10, 20)

# a_decorator is called only once, when we decorated the function.
# After that whenever we call the decorated function foo,
# it calls a wrapper function.

```

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

---

Example: A decorator that calculates and prints total execution time  
of a function.

```python
import time

def timer(func):
    """A decorator that prints how long a function took to run.

    Args:
        func (callable): The function being decorated.

    Returns:
        callable: The decorated function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        print(f"{func.__name__} function took {total_time:.4f} seconds")
        return result
    return wrapper

@timer
def delay(delay_time):
    time.sleep(delay_time)

delay(5)
print("Done :)")
```

Output

```plaintext
delay function took 5.000704526901245s
Done :)
```

---

Example: Memoize/cache results of a function.

```python
def memoize(func):
    """Store the results of the decorated function for fast lookup.

    Args:
        func (callable): The function being decorated.

    Returns:
        callable: The decorated function.
    """
    # Store results in a dictionary that maps arguments to results.
    cache = {}

    def wrapper(*args, **kwargs):
        kwargs_key = tuple(sorted(kwargs.items()))

        if (args, kwargs_key) not in cache:
            cache[(args, kwargs_key)] = func(*args, **kwargs)

        return cache[(args, kwargs_key)]

    return wrapper

@memoize
def foo(one, two, three, four, five):
    print('foo is called')
    return 99

result1 = foo(1, 2, 3, four=4, five=5)
print('result1', result1)

result2 = foo(1, 2, 3, four=4, five=5)
print('result2', result2)

result3 = foo(1, 2, 3, four=4, five=5)
print('result3', result3)
```

Output

```plaintext
foo is called
result1 99
result2 99
result3 99
```

As we can see `foo(1, 2, 3, four=4, five=5)` is called only once,  
subsequent calls to `foo(1, 2, 3, four=4, five=5)` got results from the cache.

---

Example: Example to show the type of *args & **kwargs passed to a wrapper function.

*args -> tuple

**kwargs -> dictionary

```python

def print_args(func):
    print('decorator called')
    def wrapper(*args, **kwargs):
        print(f'*args = {args}')
        print(f'**kwargs = {kwargs}')
        return func(*args, **kwargs)

    return wrapper

@print_args
def foo(one, two, three, four=4, five=5):
    return 99

result = foo(1, 2, 3, 4, 5)

print(result)

result = foo(one=1, two=2, three=3, four=4, five=5)

print(result)

result = foo(one=1, two=2, three=3)

print(result)

result = foo(1, 2, 3, four=4, five=5)

print(result)

```

---

Example: Print the return type of a function.

```python

def print_return_type(func):
    """Print the return type of a function.

    Args:
        func (callable): The function being decorated.

    Returns:
        callable: The decorated function.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} returns {type(result)} value")
        return result

    return wrapper

@print_return_type
def foo(value):
    return value

print(foo(50))
print(foo([10, 20, 30]))
print(foo({"name": "Peter Parker"}))

```

Output

```plaintext
foo returns <class 'int'> value
50
foo returns <class 'list'> value
[10, 20, 30]
foo returns <class 'dict'> value
{'name': 'Peter Parker'}
```

---

Example: Count function calls.

```python

def counter(func):
    def wrapper(*args, **kwargs):
        print('wrapper called')
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0

    return wrapper

@counter
def foo():
    return 99

print(foo())
print(foo())

print(f"foo.count = {foo.count}")

```

Output

```plaintext
wrapper called
99
wrapper called
99
foo.count = 2
```
