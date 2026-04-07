# OOP

## Python Objects

In Python, the phrase "everything is an object" means that all data—from simple numbers to complex functions and modules—is represented as an object in memory. Unlike languages like Java or C++, which distinguish between "primitive" types (like ) and objects, Python treats every value as a full-fledged object with its own identity, type, and value. [1, 2, 3]  
Core Characteristics of Python Objects 
Every object in Python possesses three fundamental properties: 

• Identity: A unique identifier that acts as the object's address in memory. You can find this using the  function. 
• Type: Defines what the object is (e.g., an integer, string, or list) and what operations it supports. Use the  
 function to inspect it. 
• Value: The actual data held by the object (e.g., the number  or the text ). [1, 5, 6, 7, 8]  

What Counts as an Object? 
In Python, the definition of an "object" is expansive: 

• Basic Data Types: Integers (), floating-point numbers (), and Booleans () are all objects. 
• Functions and Methods: You can assign functions to variables, pass them as arguments, or store them in lists because they are objects. 
• Classes: In Python, a class is not just a blueprint; the class itself is an object of type . 
• Modules: Imported modules (like  or ) are objects that contain attributes and methods. 
• None: Even the null value  is a singleton object of the  class. [1, 6, 9, 10, 11, 12, 13, 14, 15]  

Why This Matters 

• Consistency: All entities follow the same rules, allowing for powerful techniques like metaprogramming (code that manipulates other code). 
• First-Class Citizens: Because functions and classes are objects, they are "first-class," meaning they can be handled just like any other data. 
• Introspection: You can use the  
 function on almost anything to see its available attributes and methods. 

Important Exceptions 
While almost every value is an object, some parts of Python are not: 

• Keywords: Words like , , , and  are part of the language syntax and are not objects. 
• Operators: Symbols like , , and  are not objects, though they often trigger "dunder" methods (like ) on the objects they operate on. 
• Variables: In Python, a variable is merely a name (a pointer) that refers to an object; the name itself is not the object. [2, 3, 8, 16, 20, 21]  

AI responses may include mistakes.

[1] https://docs.python.org/3/reference/datamodel.html
[2] https://medium.com/@thehippieandtheboss/what-is-an-object-in-python-f38f4026a07f
[3] https://www.naukri.com/code360/library/object-in-python
[4] https://www.udacity.com/blog/2020/11/python-classes-and-objects-what-you-need-to-know.html
[5] https://blog.devgenius.io/python3-everything-is-object-220de0c3bf99
[6] https://dev.to/anik_sikder_313/everything-is-an-object-in-python-from-beginner-to-wait-what-level-582m
[7] https://learninbits.com/everything-is-an-object-in-python-explained/
[8] https://imarticus.org/blog/understanding-python-objects-a-comprehensive-guide/
[9] https://www.youtube.com/watch?v=U86ix9-gSbE
[10] https://medium.com/@ajithpmdwaraka/everything-in-python-is-an-object-42495c8b731c
[11] https://python.plainenglish.io/everything-is-an-object-in-python-so-what-2f135985f1bd
[12] https://linux.die.net/diveintopython/html/getting_to_know_python/everything_is_an_object.html
[13] https://stackoverflow.com/questions/40478536/in-python-what-does-it-mean-by-everything-is-an-object
[14] https://www.youtube.com/watch?v=_0lGCQvieV8
[15] https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Basic_Objects.html
[16] https://stackoverflow.com/questions/865911/is-everything-an-object-in-python-like-ruby
[17] https://medium.com/@thehippieandtheboss/what-is-an-object-in-python-f38f4026a07f
[18] https://www.udacity.com/blog/2020/11/python-classes-and-objects-what-you-need-to-know.html
[19] https://www.quora.com/I-read-somewhere-that-in-Python-almost-everything-is-an-object-What-are-those-things-that-are-not-considered-objects
[20] https://jakevdp.github.io/WhirlwindTourOfPython/03-semantics-variables.html
[21] https://stackoverflow.com/questions/32083871/what-does-everything-mean-when-someone-says-everything-in-python-is-an-object

---

## Methods

In Python, methods are indeed functions that are "associated" with an object or a class. While they look like regular functions, they are defined inside a class and are designed to define the behaviors and actions that an object of that class can perform. [1, 2, 3, 4, 5]  
The key characteristics that distinguish methods from standalone functions include: 
1. Definition and Association 

• Inside a Class: Unlike functions, which are defined independently at the module level, methods are always defined within a class. 
• Tied to State: Methods are intended to operate on the data (attributes) contained within a specific object or class. [6, 7, 8]  

2. The  and  Parameters 

• Instance Methods: These are the most common type. They automatically receive a reference to the specific object instance as their first argument, conventionally named . This allows the method to access or modify that specific object's attributes. 
• Class Methods: Defined using the   Python Documentation 
 decorator, these receive a reference to the class itself (conventionally ) instead of an instance. They are used for operations that involve the entire class rather than a single object. 

3. Invocation Syntax 

• Dot Notation: You typically call a method "on" an object using the dot operator (e.g., ). In contrast, a function is called directly by its name. 
• Implicit Passing: When you call , Python implicitly translates this to , passing the object  as the first argument () automatically. [1, 6, 12, 13, 14]  

4. Special Types of Methods 

• Static Methods: Defined with   Python Documentation 
, these are functions placed inside a class for organizational purposes but do not receive an implicit first argument like  or . 
• Magic (Dunder) Methods: These have double underscores before and after their names (e.g., , ). They are automatically triggered by Python for specific operations, such as object creation or string representation. [3, 5, 10, 15, 16]  

AI responses may include mistakes.

[1] https://docs.python.org/3/tutorial/classes.html
[2] http://www.w3schools.com/PYTHON/python_class_methods.asp
[3] https://pythongeeks.org/methods-in-python/
[4] https://www.geeksforgeeks.org/python/define-and-call-methods-in-a-python-class/
[5] https://study.com/academy/lesson/method-vs-function-python-overview-differences-examples.html
[6] https://techvidvan.com/tutorials/python-methods-vs-functions/
[7] https://data-flair.training/blogs/python-method/
[8] https://realpython.com/python-classes/
[9] https://www.youtube.com/watch?v=g-qRKZD3FgE
[10] https://venkyprincespace.quora.com/python-Methods-In-Python-methods-are-functions-that-are-associated-with-objects-They-define-the-behavior-or-actions
[11] https://learncsdesigns.medium.com/understanding-function-module-class-in-python-a98b323d1888
[12] https://datascienceplus.com/methods-vs-functions-in-python/
[13] https://www.reddit.com/r/learnpython/comments/15ywn4d/i_didnt_understand_what_the_difference_between/
[14] https://www.reddit.com/r/learnpython/comments/lqu1un/classes_please_explain_like_im_5/
[15] https://realpython.com/python-magic-methods/
[16] https://study.com/academy/lesson/method-vs-function-python-overview-differences-examples.html

