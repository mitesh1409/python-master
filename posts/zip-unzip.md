# zip, unzip

```python
mutants = ['charles', 'bobby', 'kurt']
powers  = ['telepathy', 'iceman', 'teleport']

# Create zip object
z1 = zip(mutants, powers)

# Unzip using * unpacking inside zip()
result1, result2 = zip(*z1)

print(result1)  # ('charles', 'bobby', 'kurt')
print(result2)  # ('telepathy', 'iceman', 'teleport')
```

---

**How `zip(*z1)` works:**

```python
z1 = [('charles', 'telepathy'), ('bobby', 'iceman'), ('kurt', 'teleport')]

zip(*z1)
# same as:
zip(('charles', 'telepathy'), ('bobby', 'iceman'), ('kurt', 'teleport'))
# → result1 = ('charles', 'bobby', 'kurt')
# → result2 = ('telepathy', 'iceman', 'teleport')
```

`*z1` unpacks the tuples as separate arguments to `zip()`, which then re-zips them in the opposite direction — effectively **transposing** the data.

> 💡 `zip(*zipped)` is the standard Python idiom for unzipping — the `*` unpacks the zipped pairs and `zip()` re-combines them column-wise.
