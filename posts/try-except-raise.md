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

---

## Example #1

Catching exceptions

Before you start writing your own custom exceptions, let's make sure you have the fundamentals of handling exceptions down.

In this exercise, you are given a function invert_at_index(x, ind) that takes two arguments, a list x and an index ind, and inverts the element of the list at that index. For example invert_at_index([5,6,7], 0) returns 1/5, or 0.2 .

Your goal is to implement error-handling to raise custom exceptions based on the type of error that occurs.

Use a try - except - except pattern (with two except blocks) inside the function to catch and handle two exceptions as follows:

* try executing the code as-is, returning 1/x[ind].
* if ZeroDivisionError occurs, print "Cannot divide by zero!",
* if IndexError occurs, print "Index out of range!"

```python

# Modify the function to catch exceptions
def invert_at_index(x, ind):
  try:
    return 1/x[ind]
  except ZeroDivisionError:
    print("Cannot divide by zero!")
  except IndexError:
    print("Index out of range!")
 
a_list = [5,6,0,7]

# Works okay
print(invert_at_index(a_list, 1))

# Potential ZeroDivisionError
print(invert_at_index(a_list, 2))

# Potential IndexError
print(invert_at_index(a_list, 5))

```

---

## Example #2

Custom exceptions

You don't have to rely solely on built-in exceptions like IndexError: you can define custom exceptions that are more specific to your application. You can also define exception hierarchies. All you need to define an exception is a class inherited from the built-in Exception class or one of its subclasses.

Earlier in the course, you defined an Employee class and used print statements and default values to handle errors like creating an employee with a salary below the minimum or giving a raise that is too large. A better way to handle this situation is to use exceptions - because these errors are specific to our application (unlike, for example, a division by zero error, which is universal), it makes sense to use custom exception classes.

* Define an empty class SalaryError inherited from the built-in ValueError class.

* Define an empty class BonusError inherited from the SalaryError class.

* Complete the definition of __init__() to raise a SalaryError with the message "Salary is too low!" if the salary parameter is less than MIN_SALARY class attribute.

* Implement exceptions in the give_bonus() method: raising a BonusError if the bonus amount is larger than the class' MAX_BONUS, and raising a SalaryError if the result of adding the bonus would be lower than the class' MIN_SALARY.

```python

# Define SalaryError inherited from ValueError
class SalaryError(ValueError):
    pass


# Define BonusError inherited from SalaryError
class BonusError(SalaryError):
    pass

class Employee:
  MIN_SALARY = 30000
  MAX_RAISE = 5000

  def __init__(self, name, salary = 30000):
    self.name = name

    # If salary is too low
    if salary < Employee.MIN_SALARY:
      # Raise a SalaryError exception
      raise SalaryError("Salary is too low!")

    self.salary = salary

  # Raise exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
      raise BonusError("The bonus amount is too high!")  

    elif self.salary + amount < Employee.MIN_SALARY:
      raise SalaryError("The salary after bonus is too low!")

    self.salary += amount

```
