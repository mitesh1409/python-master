# Mutable, Immutable

Q: Is there an easy way to tell if a variable is immutable or mutable?

A: Well…there’s the rule: numbers, strings, booleans, and tuples are immutable, whereas most everything else is mutable (such as  
lists, sets, and dictionaries). Things can get a little more complicated if you try to determine this at runtime. One possible technique is  
to pass your variable to the hash built-in. If the passed-in variable is immutable, hash returns a number. If the passed-in variable is  
mutable, hash fails with a TypeError, which you’d have to code for with some sort of exception-handling code. But, we might be  
getting ahead of ourselves here…

What is mutable?  

* lists
* sets
* dictionaries

What is immutable?  

* numbers
* strings
* booleans
* tuples

Reference:  
Book: Head First Python 3rd Edition
