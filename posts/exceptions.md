# Exceptions

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
