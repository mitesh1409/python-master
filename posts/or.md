# The "or" keyword

- `or` = check if one (**or more**) condition is met
- `or` is the same as Logical OR `||` operator in other programming languages
- Use when any of several options are acceptable

```python
pasta_quantity = 600
olive_oil_quantity = 30

# Check if we have enough of EITHER ingredient
if pasta_quantity >= 500 or olive_oil_quantity >= 30:
    print(True)
else:
    print(False)
```

**Output:**
```
True
```
