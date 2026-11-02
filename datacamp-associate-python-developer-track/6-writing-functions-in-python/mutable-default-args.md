# Mutable default arguments are dangerous.

```python
# Bad/Incorrect
def foo(temp_list=[]):
    temp_list.append(10)
    return temp_list

print(foo())

print(foo())

# Good/Correct
def bar(temp_list=None):
    if temp_list == None:
        temp_list = []
    temp_list.append(10)
    return temp_list

print(bar())

print(bar())
```

---

**Mutable or immutable?**

The following function adds a mapping between a string and the lowercase version of that string  
to a dictionary. What do you expect the values of d and s to be after the function is called?

```python
def store_lower(_dict, _string):
  """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`

  Args:
    _dict (dict): The dictionary to update.
    _string (str): The string to add.
  """
  orig_string = _string
  _string = _string.lower()
  _dict[orig_string] = _string

d = {}
s = 'Hello'

store_lower(d, s)
```
