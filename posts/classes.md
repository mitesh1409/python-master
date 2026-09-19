# Classes

When we think we need to define a new class, we work though a series of questions in  
an effort to convince ourselves we actually need one. Here’s what we ask:

#1 Will a dictionary do instead?  
If all you need is a way to bundle named data values together,  
use a dictionary not a class.  
You’ll be much happier.

#2 What about defining a class using the built-in `dataclass`?  
The PSL contains a module called `dataclass`. This module exists to make it easy to  
create a custom class in Python with the minimum of effort.

#3 What about using the third-party `attrs` package?  
PyPI contains the very highly regarded `attrs`, which can be considered to be a  
superset of the built-in `dataclass`. Like the latter, it works hard to help you  
avoid writing all the boilerplate code required to create your own custom class.  

If you end up answering no, no, and no to these three questions,  
feel free to create your own custom class.  

The Python documentation (especially [Chapter 9 of The Python
Tutorial](https://docs.python.org/3/tutorial/classes.html)) is a good starting point.
