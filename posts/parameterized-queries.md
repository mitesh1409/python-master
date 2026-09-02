# Parameterized Queries in Python

Python database engines support the notion of  
parameterized queries/statements. The use of  
placeholders can protect your code from all manner  
of SQL Injection Attacks, and the use of placeholders  
is strongly encouraged. Using f-strings to achieve the  
same effect (i.e., parameterized queries/statements)  
might lead to a world of pain… just don’t try and say  
we didn’t warn you.

Most placeholder technologies expect data to be  
passed into SQL queries using a tuple, even when  
there’s only one parameter. This can lead to weird  
looking tuples. Remember (42,), which looks weird, but works.
