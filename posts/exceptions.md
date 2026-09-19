# Errors/Exceptions

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
| Errors | Avoid errors being produced | Will produce an error |
| Subsequent code | Still execute subsequent code | Avoid executing subsequent code |
