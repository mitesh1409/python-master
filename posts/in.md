# The "in" keyword

- `in` = check if a value is **in** a variable/data structure
- It is faster than looping through every key.  

```python
recipe = {"pasta": 500, "tomatoes": 400,
          "garlic": 15, "basil": 20}

if "pasta" in recipe.keys():
    print(True)
else:
    print(False)
```

**Output:**
```
True
```
