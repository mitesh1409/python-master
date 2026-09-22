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

```python
ingredients = ["pasta", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Access every second element
print(ingredients[::2])

# Access every third element, starting at the second
print(ingredients[1::3])
```

Reference:  
Book: Head First Python 3rd Edition

---

Lists in Python are mutable, allowing you to add, remove, or modify elements.  

Key points:  

* **Creating Lists**: You saw how to create a list to store a collection of items, such as different types of cookies you've eaten over a week.

* **Adding Elements**: Using the .append() method to add individual items to a list and the .extend() method to combine multiple lists into one.

* **Accessing and Removing Elements**: You learned how to access elements in a list using their index and how to remove elements with the .pop() method, which requires the index of the element you wish to remove.

* **Finding Elements**: The .index() method was introduced as a way to find the position of an item in a list.

* **Iterating Over Lists**: You explored how to use list comprehensions to iterate over each element in a list, performing operations like converting strings to title case.

* **Sorting Lists**: Lastly, you learned how to use the sorted() function to return a new list with elements in order, such as sorting cookie names alphabetically.
