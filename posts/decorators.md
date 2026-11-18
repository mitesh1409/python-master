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

---

One of the problems with decorators is that they obscure the decorated function's metadata.  

Check the following example.

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

@timer # While using decorator, function metadata is not available.
def sleep_n_seconds(n=10):
    """Pause processing for n seconds.

    Args:
        n (int): The number of seconds to pause for.

    Returns:
        None
    """
    time.sleep(n)

sleep_n_seconds(2)

print('Done :)')

print(f"""
sleep_n_seconds.__name__
{sleep_n_seconds.__name__}
""")

print(f"""
sleep_n_seconds.__doc__
{sleep_n_seconds.__doc__}
""")

print(f"""
sleep_n_seconds.__defaults__
{sleep_n_seconds.__defaults__}
""")

```

To understand why we have to examine the timer() decorator. Remember that when we write decorators, we almost always define a nested function to return. Because the decorator overwrites the sleep_n_seconds() function, when you ask for sleep_n_seconds()'s docstring or name, you are actually referencing the nested function that was returned by the decorator. In this case, the nested function was called wrapper() and it didn't have a docstring.

Fortunately, Python provides us with an easy way to fix this. The wraps() function from the functools module is a decorator that you use when defining a decorator. If you use it to decorate the wrapper function that your decorator returns, it will modify wrapper()'s metadata to look like the function you are decorating. Notice that the wraps() decorator takes the function you are decorating as an argument.

```python

import time
from functools import wraps

def timer(func):
    """A decorator that prints how long a function took to run.

    Args:
        func (callable): The function being decorated.

    Returns:
        callable: The decorated function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        print(f"{func.__name__} function took {total_time:.4f} seconds")
        return result
    return wrapper

@timer
def sleep_n_seconds(n=10):
    """Pause processing for n seconds.

    Args:
        n (int): The number of seconds to pause for.

    Returns:
        None
    """
    time.sleep(n)

sleep_n_seconds(2)

print('Done :)')

print(f"""
sleep_n_seconds.__name__
{sleep_n_seconds.__name__}
""")

print(f"""
sleep_n_seconds.__doc__
{sleep_n_seconds.__doc__}
""")

print(f"""
sleep_n_seconds.__defaults__
{sleep_n_seconds.__defaults__}
""")

```

---

Example

Measuring decorator overhead
Your boss wrote a decorator called check_everything() that they think is amazing, and they are insisting you use it on your function. However, you've noticed that when you use it to decorate your functions, it makes them run much slower. You need to convince your boss that the decorator is adding too much processing time to your function. To do this, you are going to measure how long the decorated function takes to run and compare it to how long the undecorated function would have taken to run. This is the decorator in question:

```python

from functools import wraps

def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    check_outputs(result)
    return result
  return wrapper

@check_everything
def duplicate(my_list):
  """Return a new list that repeats the input twice"""
  return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

```

How to get the wrapped/original function from the decorated function?  

```python

from functools import wraps

def print_hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Hello :)')
        return func(*args, **kwargs)
    return wrapper

@print_hello
def foo():
    print('foo called')

print('Calling decorated function foo')
foo()

print('\n\n')

print('Calling original function foo')
foo.__wrapped__()

```

---

Decorators that take arguments

```python

def run_three_times(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)
    return wrapper

@run_three_times
def greetings(message="Hello"):
    print(message)

greetings()

```

Here `run_three_times` decorator runs the function 3 times.  
It is static/hard-coded, what if we want to run function 'n' times, dynamically.  

Somehow we need to pass arguments to a decorator function.  
But a decorator is only supposed to take one argument - the function it is decorating.  
Also, when you use decorator syntax, you're not supposed to use the parentheses.

Solution = A decorator factory

To make run_n_times() work, we have to turn it into a function that returns a decorator,  
rather than a function that is a decorator.  
So let's start by redefining run_n_times() so that it takes n as an argument,  
instead of func.  
Then, inside of run_n_times(), we'll define a new decorator function.  
This function takes "func" as an argument because it is the function that will  
be acting as our decorator.  
We start our new decorator with a nested wrapper() function, as usual.  
Now, since we are still inside the run_n_times() function, we have access to the n  
parameter that was passed to run_n_times().  
We can use that to control how many times we repeat the loop that calls  
our decorated function.  
As usual for any decorator, we return the new wrapper() function.  
And, if run_n_times() returns the decorator() function we just defined,  
then we can use that return value as a decorator.  
Notice how when we decorate print_sum() with run_n_times(), we use parentheses after  
@run_n_times. This indicates that we are actually calling run_n_times() and decorating  
print_sum() with the result of that function call.  
Since the return value from run_n_times() is a decorator function,  
we can use it to decorate print_sum().

```python

# Decorator Function
# It takes only func as an argument.
def run_three_times(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            func(*args, **kwargs)
    return wrapper

@run_three_times
def greetings(message="Good morning!"):
    print(message)

greetings()

# Decorator Factory that returns a Decorator Function.
# It can take one or more arguments, that we can use inside the Decorator Function.
def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@run_n_times(3)
def say_hello():
    print('Hello')

say_hello()

```

When we use decorator syntax, the thing that comes after the @ symbol must be  
a reference to a decorator function.  
We can use the name of a specific decorator, or we can call a function that  
returns a decorator.

---

```python

from functools import wraps

def suit_up(threat=False):
    def decorator(func):
        """Suit up for your next task"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            if threat:
                print(f'{func.__name__}, suit up & save the world!')
            else:
                print(f'{func.__name__}, wear Tuxedo and take MJ to a dinner party!')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@suit_up(True)
def spiderman():
    print('spiderman called')

spiderman()
spiderman()

```

---

HTML Generator

You are writing a script that generates HTML for a webpage on the fly. So far, you have written two decorators that will add bold or italics tags to any function that returns a string. You notice, however, that these two decorators look very similar. Instead of writing a bunch of other similar looking decorators, you want to create one decorator, html(), that can take any pair of opening and closing tags.

```python

def bold(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<b>{}</b>'.format(msg)
  return wrapper

def italics(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    msg = func(*args, **kwargs)
    return '<i>{}</i>'.format(msg)
  return wrapper

```

```python

def html(open_tag, close_tag):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      msg = func(*args, **kwargs)
      return '{}{}{}'.format(open_tag, msg, close_tag)
    # Return the decorated function
    return wrapper
  # Return the decorator
  return decorator

# Make hello() return bolded text
@html('<b>', '</b>')
def hello(name):
  return 'Hello {}!'.format(name)
  
print(hello('Alice'))

# Make goodbye() return italicized text
@html('<i>', '</i>')
def goodbye(name):
  return 'Goodbye {}.'.format(name)
  
print(goodbye('Alice'))

# Wrap the result of hello_goodbye() in <div> and </div>
@html('<div>', '</div>')
def hello_goodbye(name):
  return '\n{}\n{}\n'.format(hello(name), goodbye(name))
  
print(hello_goodbye('Alice'))

```

---

Example: timeout decorator

```python

import time
import signal
from functools import wraps

def timeout_in_5s(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Set an alarm for 5 seconds
        signal.alarm(5)

        try:
            return func(*args, **kwargs)
        finally:
            # Cancel alarm
            signal.alarm(0)
    return wrapper

@timeout_in_5s
def foo():
    time.sleep(2)
    print('foo!')

foo()

```


```python

import time
import signal
from functools import wraps

def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Set an alarm for n_seconds seconds
            signal.alarm(n_seconds)

            try:
                return func(*args, **kwargs)
            finally:
                # Cancel alarm
                signal.alarm(0)
        return wrapper
    return decorator

@timeout(3)
def foo():
    time.sleep(1)
    print('foo!')

foo()

@timeout(2)
def bar():
    time.sleep(1)
    print('bar!')

bar()

```

---

Tag your functions

Tagging something means that you have given that thing one or more strings that act as labels. For instance, we often tag emails or photos so that we can search for them later. You've decided to write a decorator that will let you tag your functions with an arbitrary list of tags. You could use these tags for many things:

Adding information about who has worked on the function, so a user can look up who to ask if they run into trouble using it.
Labeling functions as "experimental" so that users know that the inputs and outputs might change in the future.
Marking any functions that you plan to remove in a future version of the code.
Etc.

```python

def tag(*tags):
  # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)

```

---

Check the return type

Python's flexibility around data types is usually cited as one of the benefits of the language. It can sometimes cause problems though if incorrect data types go unnoticed. You've decided that in order to ensure your code is doing exactly what you want it to do, you will explicitly check the return types in all of your functions and make sure they're returning what you expect. To do that, you are going to create a decorator that checks if the return type of the decorated function is correct.

Note: `assert` is a keyword that you can use to test whether something is true. If you type `assert condition` and `condition` is `True`, this function doesn't do anything. If condition is `False`, this function raises an error. The type of error that it raises is called an `AssertionError`.

```python

def returns_dict(func):
  # Complete the returns_dict() decorator
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    assert type(result) == dict
    return result
  return wrapper
  
@returns_dict
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')

```

```python

def returns(return_type):
  # Complete the returns() decorator
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      assert type(result) == return_type
      return result
    return wrapper
  return decorator
  
@returns(dict)
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')

```
