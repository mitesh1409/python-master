# Lists

Unlike with arrays, where you  
typically have to say how big your array is likely  
to get (e.g., 1,000 slots) and what type of data it’s  
going to contain (e.g., integers), there’s no need to  
declare either of these with your Python lists.  

Python lists are dynamic, which means they grow  
as needed (so there’s no need to predeclare the  
number of slots beforehand). And Python lists  
don’t contain data values, they contain object  
references, so you can put any data of any type  
in a Python list. You can even mix’n’match types.  

Python lists are heterogeneous, which means they can contain different types of data.  

Python lists are mutable, which means you can change the contents of a list after it’s been created. You can add, remove, or change items in a list.

Although lists come with a handy `sort` method, be  
careful using it as the ordering is applied in-place.  
If you want to keep any list’s current order, use the  
`sorted` BIF instead (which always returns a sorted  
copy of your data).  

`sort` - this is called on a list instance and changes the current order of list items,  
the original order of list items is lost.  
`sorted` - `sorted` is called by passing list instance as an argument, it returns a copy of the sorted list items, the original order of the list items remains as it is.  
``

Reference:  
Book: Head First Python 3rd Edition
