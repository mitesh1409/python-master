# continue, break, pass

The exact equivalent of the continue statement in Python is the continue keyword itself. It behaves exactly the same way as it does in languages like C, C++, Java, and JavaScript—it immediately skips the rest of the code inside the current loop iteration and jumps straight to the next cycle.

## Code Example

```python
for number in range(1, 6):
    if number == 3:
        continue  # Skips the rest of the loop block for number 3
    print(number)
```

```plaintext
Output:

1
2
4
5
```

## Key Differences: continue vs. break vs. pass

It is common to mix these three control flow statements up, but they have completely different behaviors:

| Keyword | What it does | Impact on the Loop |
|---|---|---|
| continue | Skips the remaining code in the current iteration only. | Moves directly to the next loop cycle. |
| break | Terminates the loop entirely. | Exits the loop block immediately. |
| pass | Does absolutely nothing; acts as a null syntax placeholder. | The loop continues executing exactly as normal. |

If you are using continue inside a while loop, always make sure your loop counter increments before the continue statement runs, otherwise you will accidentally trigger an infinite loop.
