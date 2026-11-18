# Context Manager

A context manager function is technically a generator that yields  
a single value.

---

How to create a context manager

```python
@contextlib.contextmanager # 5 - Add the `@contextlib.contextmanager` decorator.
def my_context(): # 1 - Define a function.
  # 2 - (optional) Add any set up code your context needs.
  yield # 3 - Use the "yield" keyword.
  # 4 - (optional) Add any teardown code your context needs.
```

1. Define a function.
2. (optional) Add any set up code your context needs.
3. Use the "yield" keyword.
4. (optional) Add any teardown code your context needs.
5. Add the `@contextlib.contextmanager` decorator.

---

Example: Party organizer context manager

Good example to understand context manager.

```python
import contextlib

@contextlib.contextmanager
def party_organizer(theme, food_menu, drinks_menu):
    # Setup
    decorate(theme)
    arrange_food_stalls(food_menu)
    arrange_drink_stalls(drinks_menu)
    arrange_music_dj()

    try:
        yield
    finally:
        # Teardown
        remove_decoration()
        remove_food_stalls()
        remove_drink_stalls()
        remvoe_music_dj()
        cleanup_site()

# Lets do party with the help of party organizer
with party_organizer(theme, food_menu, drinks_menu):
    party()
```

---

Example: Execution timer context manager.

```python
import contextlib
import time

@contextlib.contextmanager
def exec_timer():
    start = time.perf_counter()   # setup

    try:
        yield
    finally:                      # teardown runs even if the block raises
        end = time.perf_counter()
        print(f"Execution time: {end - start:.4f} seconds")


with exec_timer():
    sum(range(10_000_000))
# Execution time: 0.1832 seconds
```

`time.perf_counter()` is the right clock for measuring durations (high resolution, not affected by system clock changes). `time.time()` works but is less precise.

The `try/finally` matters: without it, if the code inside the `with` block raises an exception, the code after `yield` never runs and nothing gets logged.

---

**Can we yield the execution time?**

You're right that we can't yield the final time **directly**, because the time isn't known until after the `with` block finishes, and the code after `yield` only runs at that point.

But there's a common workaround: **yield a mutable object** that you fill in during teardown:

```python
import contextlib
import time

@contextlib.contextmanager
def exec_timer():
    result = {}                   # mutable container
    start = time.perf_counter()
    try:
        yield result              # caller gets a reference to it
    finally:
        result["elapsed"] = time.perf_counter() - start


with exec_timer() as t:
    sum(range(10_000_000))

print(t["elapsed"])   # available after the with block ends
```

The caller receives `result` at the `yield`, and the dict gets populated after the block exits. This works because both sides hold a reference to the same object.

---

**Alternative: a class-based context manager** (often cleaner for this):

```python
import time

class ExecTimer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        return False              # don't suppress exceptions


with ExecTimer() as t:
    sum(range(10_000_000))

print(t.elapsed)
```

Here `t.elapsed` is a clean attribute instead of a dictionary key.

---

**Which to use?**

| | `@contextmanager` | Class-based |
|---|---|---|
| Code size | Shorter | Longer |
| Return a value after the block | Needs a mutable workaround | Natural (attributes) |
| Best for | Simple setup/teardown | When you need to expose results |

---

> 💡 For logging in real projects, use the `logging` module instead of `print`, e.g. `logging.info("Execution time: %.4f s", elapsed)`, so you can control levels and output destinations.

---

```python
import contextlib

@contextlib.contextmanager
def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)
```
