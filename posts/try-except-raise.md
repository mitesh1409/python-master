# Errors/Exceptions, `try`-`except` & `raise`

## `try`-`except`-`else`-`finally`

```python
try:
    # Try to execute code that might raise an error
    # Code that might raise an exception
    # e.g., result = int(user_input)
    pass

except Exception as e:
    # What to do in case of failure, goes here.
    # Runs ONLY if an error occurs inside the try block.
    # Note: It's best practice to catch specific exceptions 
    # (e.g., except ValueError:) rather than generic Exception.
    print(f"An error occurred: {e}")

else:
    # What to do in case of success, goes here.
    # Runs ONLY if the try block executed successfully 
    # (i.e., no exceptions were raised).
    print("Executed successfully with no errors!")

finally:
    # Final todos at the end, clean-up tasks, regardless of success/failure.
    # Runs NO MATTER WHAT. 
    # Ideal for cleanup tasks like closing files, database connections, 
    # or releasing resources.
    print("Cleanup: This always runs.")
```

---

## Critical anti-pattern - the bare `except:` clause

Avoid Bare `except:`

Using `except:` without specifying an error type catches **every single exception**, including system-level events like `KeyboardInterrupt` (when you press `Ctrl + C` to stop a script) or `SystemExit`. This makes your program very hard to debug and stop.

Instead, you should catch `Exception` broadly (if you want to catch all standard errors) or, even better, catch **specific exceptions** (like `ValueError` or `KeyError`).

---

## Summary of When Each Block Runs:

| Block | When does it run? | Common Use Case |
| --- | --- | --- |
| **`try`** | Always runs first. | Putting risky code that might fail. |
| **`except`** | **Only** if an error occurs in `try`. | Handling the error gracefully or logging it. |
| **`else`** | **Only** if *no* error occurs in `try`. | Running code that depends on the `try` block succeeding. |
| **`finally`** | **Always**, right before leaving the statement. | Cleaning up resources (closing files, network sockets). |

---

Never hope for the best, ignore runtime exceptions, nor keep going.  
A better strategy is to catch the raised exception before it stops your code.  
You can do this with Python’s try… except… mechanism.

Here’s an example of try in action:  

```python
...

# We are calculating some value by (accidently) dividing it with zero.
value = 1 / 0

...
```

This code is going to throw `ZeroDivisionError` built-in Python exception.  
And since we did not handle this exception, the application will crash.  

Lets do exception handling then,  

```python
...

try:
    value = 1 / 0
except ZeroDivisionError:
    print("Division by zero")
except:
    print("Something else has gone terribly wrong (gulp).")

...
```

Using “try” with an “except” lets you ask for  
forgiveness. The raised exception is caught and  
dealt with (and there’s no crash).  

---

Do error handling using `try-except`.  

Raise error using `raise`.  

---

What is an Error?  

* Code that violates a rule
* Error = Exception
* Cause our program to terminate

Notice that the error outputs mentions the word "Traceback"?  
A traceback can be thought of as a report.  

A traceback provides following information:  

* What type of error occurred? Type and description.
* Where it occurred in our code? Provides line number.
* Complete stack trace.

> While checking a Traceback, first check the bottom section,  
> it provides the most useful information regarding the error/exception.  

> Key traceback reading rule: Always read from the bottom up for the error message,  
> but look at the top to find where in your own code the mistake is.  

---

try-except vs. raise  

| | `try` - `except` | `raise` |
|---|---|---|
| Purpose | Error handling | Produce/raise an error/exception |
| Errors | Avoid errors being produced | Will produce/raise an error |
| Subsequent code | Still execute subsequent code | Avoid executing subsequent code |

---

https://docs.python.org/3/library/exceptions.html#exception-hierarchy
