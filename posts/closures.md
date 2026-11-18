# Closures

A closure in Python is a tuple of variables that are no longer in scope,  
but that a function needs in order to run.

A closure is a function together with the variables it captured from the enclosing scope. Those variables aren't really "out of scope". They stay alive because the inner function keeps a reference to them.

---

Example: Counter

```python
def counter():
    count = 0

    def increment_counter():
        nonlocal count
        count += 1
        return count

    return increment_counter

counter_one = counter()

print(f'counter_one.__closure__ = {counter_one.__closure__}')

print(counter_one.__closure__[0])

print(counter_one.__closure__[0].cell_contents)

print(counter_one)

counter_value = counter_one()
counter_value = counter_one()
counter_value = counter_one()
counter_value = counter_one()

print(f"Counter one = {counter_value}")

print('=' * 40)

counter_two = counter()

print(counter_two)

counter_value = counter_two()
counter_value = counter_two()

print(f"Counter two = {counter_value}")
```

---

Example: Mission impossible style self destructible message.

```python
def border():
    print('=' * 40)

def relay_message_once():
    # We might get this from an API call or set a static message.
    message = 'Some message text...'
    relayed = False

    print('inside relay_message_once')
    print(f"message = {message}")
    print(f"relayed = {relayed}")

    def relay():
        nonlocal message, relayed

        print('inside relay')
        print(f"message = {message}")
        print(f"relayed = {relayed}")

        # Message already relayed then return None
        if relayed:
            return

        # Set response
        response = message
        # Destroy message
        message = None
        # Mark it as relayed
        relayed = True

        return response

    return relay

relay_message = relay_message_once()
print(relay_message)
border()

print(relay_message())
border()

print(relay_message())
border()

print(relay_message())
border()
```

---

```python
def foo():
  print('foo v1')

def get_new_func(func):
  def call_func():
    func()
  return call_func

new_func = get_new_func(foo)

# Redefine foo
def foo():
  print('foo v2')

del(foo)

new_func() # foo v1
new_func() # foo v1
new_func() # foo v1
```

Here `call_func` closure has access to v1 of `foo` function.  

Even if you delete `foo`, `call_func` closure has access to v1 of `foo` function.  

---

```python
def foo():
  print('foo v1')

def get_new_func(func):
  def call_func():
    func()
  return call_func

# Overwrite `foo` with the new function
foo = get_new_func(foo)

foo()
```

---

`__closure__` is a tuple of **cell objects**, and each cell holds the value in its `cell_contents` attribute:

```python
def counter():
    count = 0

    def increment_counter():
        nonlocal count
        count += 1
        return count

    return increment_counter

counter_one = counter()

print(counter_one.__closure__[0].cell_contents)  # 0

counter_one()
counter_one()

print(counter_one.__closure__[0].cell_contents)  # 2
```

The cell is live: it always reflects the **current** value of `count`, not a snapshot from when the closure was created.

---

**Mapping variable names to cells:**

If a function has several closure variables, `__code__.co_freevars` gives the names, in the same order as `__closure__`:

```python
def make_adder(a, b):
    def add(x):
        return x + a + b
    return add

add_fn = make_adder(10, 20)

print(add_fn.__code__.co_freevars)   # ('a', 'b')

for name, cell in zip(add_fn.__code__.co_freevars, add_fn.__closure__):
    print(name, "=", cell.cell_contents)
# a = 10
# b = 20
```

---

**Closures are independent per call:**

```python
c1 = counter()
c2 = counter()

c1(); c1()
c2()

print(c1.__closure__[0].cell_contents)  # 2
print(c2.__closure__[0].cell_contents)  # 1
```

Each call to `counter()` creates its own `count` cell.

---

**Two notes:**

- `cell_contents` is writable (Python 3.7+), but modifying it from outside is hacky. It's meant for **inspection and debugging**, not normal program logic.
- If a cell is empty (the variable isn't assigned yet), accessing `cell_contents` raises `ValueError`.

---

> `__closure__` is a tuple of **cells**, but the closure concept itself is the function together with the variables it captured from the enclosing scope. Those variables aren't really "out of scope". They stay alive because the inner function keeps a reference to them.
