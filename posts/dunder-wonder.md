# dunder, wonder

Python programmers shorten “double underscore
add double underscore” to simply “dunder add.” If you hear
someone refer to a method as “dunder exit,” what they are actually
referring to is __exit__. All of these (as a group) are called
“the dunders.” Further, any method which starts with a single
underscore is known as a “wonder” (and—yes—it is a perfectly
acceptable reaction to groan at all of this).

It’s just not possible to ignore the dunders when creating Python classes.  

Another place where the dunders shine is in relation to the `with` statement.  
Two dunders, `__enter__` and `__exit__`, provide hooks into any `with` statement’s  
setup and teardown mechanism. 

Reference:  
Book: Head First Python 3rd Edition
