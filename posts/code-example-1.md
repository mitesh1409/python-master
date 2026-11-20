# Code Example

This is the classic "modifying a list while iterating over it" bug.

```python
def remove_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)

    return numbers

numbers_1 = [2, 4, 6, 7, 8, 9]
print(remove_even_numbers(numbers_1))
print(numbers_1)

def remove_even_numbers_v2(numbers):
    odd_numbers = []
    for number in numbers:
        if number % 2 != 0:
            odd_numbers.append(number)

    return odd_numbers

numbers_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(remove_even_numbers_v2(numbers_2))
print(numbers_2)

numbers_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
odds = [number for number in numbers_3 if number % 2 != 0]
print(odds)
print(numbers_3)
```

Step by step trace:

| Iteration | Index | List before | Item at index | Action |
|---|---|---|---|---|
| 0 | 0 | `[2, 4, 6, 7, 8, 9]` | 2 | removed |
| 1 | 1 | `[4, 6, 7, 8, 9]` | 6 | removed |
| 2 | 2 | `[4, 7, 8, 9]` | 8 | removed |
| 3 | 3 | `[4, 7, 9]` | none | loop ends |

**Why it goes wrong:** the list iterator keeps an internal index and just increments it. When you remove an item, everything after it shifts left, so the element that slid into the removed slot is **skipped**. That is why `4` and `6` (right after `2` and `4` were removed) never got checked, and `4` survives in the output even though it is even.

---

**Correct approaches:**

**1. List comprehension (best, creates a new list):**
```python
def remove_even_numbers(numbers):
    return [n for n in numbers if n % 2 != 0]

print(remove_even_numbers([2, 4, 6, 7, 8, 9]))  # [7, 9]
```

**2. Iterate over a copy, modify the original:**
```python
def remove_even_numbers(numbers):
    for number in numbers[:]:      # numbers[:] is a shallow copy
        if number % 2 == 0:
            numbers.remove(number)
    return numbers
```

**3. In-place with slice assignment (keeps the same list object):**
```python
def remove_even_numbers(numbers):
    numbers[:] = [n for n in numbers if n % 2 != 0]
    return numbers
```

---

**Side effect to notice:** your original function mutates the list passed in by the caller, because `numbers` is a reference to the same list object. Options 1 returns a new list and leaves the caller's list untouched, which is usually the safer behavior.

> 💡 **Rule of thumb:** never add or remove items from a list while looping over it. Build a new list (comprehension or `filter`) or loop over a copy. The same applies to dicts, where changing size during iteration raises `RuntimeError: dictionary changed size during iteration`.
