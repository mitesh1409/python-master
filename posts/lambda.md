# Lambda functions

- `lambda` keyword
  - Represents an *anonymous function*
  - Lambda functions are similar to arrow functions in JavaScript

```python
lambda arguments: expression
```

- Convention is to use `x` for a single argument.
- The `expression` is the equivalent of the function body.
- No `return` statement is required.
- **Can** be stored as a variable, so that it can be reused later.

---

Using lambda functions  

```python
# Get the average.
(lambda x: sum(x) / len(x))([1, 3, 5])

# Print the average.
print((lambda x: sum(x) / len(x))([1, 3, 5]))
```

---

Storing and calling a lambda function  

```python
# Store lambda function as a variable
average = lambda x: sum(x) / len(x)

# Call the average function
print(average([3, 6, 9]))
```

Output:  

```
6
```

---

Lambda function with multiple parameters  

```python
power = lambda x, y: x**y

print(power(2, 3))
```

Output:  

```
8
```

---

Lambda functions with iterables

- `map()` applies a function to **all** elements in an iterable

```python
names = ["john", "sally", "leah"]

# Apply a lambda function inside map()
capitalize = map(lambda x: x.capitalize(), names)
print(capitalize)

# OR
capitalize = lambda x: x.capitalize()
result = map(capitalize, names)
print(result)
```

**Output:**

```
<map object at 0x7fb200529c10>
```

```python
# Convert to a list
print(list(capitalize))
```

**Output:**

```
['John', 'Sally', 'Leah']
```

---

Custom vs. lambda functions  

| Scenario | Function Type |
|---|---|
| Complex task | Custom |
| Same task several times | Custom |
| Performed once | Lambda |
| Simple task | Lambda |
