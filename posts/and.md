# The "and" keyword

- `and` = check if **multiple conditions** are met
- `and` is the same as Logical AND `&&` operator in other programming languages
- Use when multiple requirements must be met

```python
pasta_quantity = 600
olive_oil_quantity = 30

# Check if we have enough of BOTH ingredients
if pasta_quantity >= 500 and olive_oil_quantity >= 30:
    print(True)
else:
    print(False)
```

**Output:**
```
True
```
