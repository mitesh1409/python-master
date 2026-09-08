# The Walrus Operator

The := operator is officially called an assignment expression, but is known the  
world over as the walrus operator. What the walrus operator lets you do is combine  
an assignment and expression together, typically replacing two lines of code with one.  

Here’s a quick (and totally contrived) example:  

Without Walrus Operator  

```python
import random

# Assignment
random_num = random.randint(0, 10)

# Expression
if random_num < 5:
    print(f"{random_num} is less than 5!")
else:
    print(f"{random_num} is 5 or greater!")
```

With Walrus Operator  

```python
import random

# Assignment + Expression
if (random_num := random.randint(0, 10)) < 5:
    print(f"{random_num} is less than 5!")
else:
    print(f"{random_num} is 5 or greater!")
```

The assignment expression combination.  
The use of the walrus operator lets  
you assign to the variable then test  
against its value in one go, and on one  
line.

The name “walrus” has come from how the operator is viewed.  
If you look at the operator, then tilt your head to the left,  
you end up looking at something that has two eyes and two big teeth.  
It looks sort of like a walrus...  
