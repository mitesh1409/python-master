# Super 4 Data Structures with built-in support in Python

Python has excellent built-in support for the following data structures:  

1. Lists
2. Tuples
3. Sets
4. Dictionaries

Lists similar to Arrays  

#1
Lists are like regular arrays on steroids.  
What differentiates a list from an array (in Python, anyway) is their ability  
to shrink and grow to any size dynamically. Python handles all the messy memory  
management details for you.  

#2
Lists are a sequenced collection of Python objects.  
You can put anything in a list slot—anything. As everything in Python is an object,  
any object can be stored in a list, with each slot numbered with an index value that  
starts from zero.

#3
Lists are a perfect fit when the order of your data is important to you.  
If you need to keep your data in a specific order, there is no better data structure  
to use than a list (even though you could also use a tuple but, remember: tuples are immutable).  

#4
Lists can be processed in many different ways.  
You can work with the data in any list using the square bracket notation,  
the list methods, Python’s BIFs, and loops (with Python’s for loop a near perfect fit here).  

When order of data is important, Lists are better.

Time complexity of an item look-up is O(n) (sequential search).  

Lists are mutable.

---

Dictionaries similar to Associative Array, Map, Hash, or Symbol Table.  

Dictionaries associate keys with values,  
and (like lists) can dynamically shrink and grow to any size.

#1
Dictionaries are like a two-columned list.  
But unlike lists, which use a numeric index to identify the slots that contain objects,  
dictionaries use keys to identify values, with the values being any Python object.

#2
A dictionary can contain any number of rows of data.  
Each key/value pair represents a row of data: a key is associated with a value.  
Just like indices in lists are unique, dictionary keys need to be unique for the lookup to work.

#3
Dictionaries provide speedy lookup functionality.  
When provided with a key, your dictionary looks up and returns the associated value.  
Thanks to the underlying implementation, these lookups do not use sequential searching.  

#4
Dictionaries can be processed in many different ways.  
You can work with the data in any dictionary using a dictionary-specific version  
of the square bracket notation, the dictionary methods, Python’s BIFs, and loops.

When look-up is important in data then Dictionaries are the best.

Time complexity of an item look-up is O(1).

Dictionaries are mutable.

---

Dictionaries are preferred over Lists when you need frequent lookups.  
Same concept applies in JavaScript too where  
Map / Object lookup is O(1) vs Array.includes() which is O(n).
