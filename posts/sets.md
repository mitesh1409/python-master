# Sets

Sets in Python  

* Contain unique data, can't have duplicates.
* Immutable/Unchangeable.
    * Can add/remove values, can't change them.
* Ideal to identify and remove duplicates.
* Quick to search (compared to other data structures such as lists).
* Don't have an index, can't use `[]` to subset.

We can convert a list to a set using `set()` built-in function.  
This process is called casting a list to a set.  

```python
# Existing list variable
ingredients_list = ["pasta", "tomatoes", "garlic", "basil",
                    "olive oil", "pasta", "salt", "garlic"]

# Convert to a set
unique_ingredients = set(ingredients_list)

# Check the data type
type(unique_ingredients) # <class 'set'>
```

Sorting a set  

To sort a set we can use built-in function `sorted()`, pass a set into it,  
it returns a list of sorted items.  
The original set remains unchanged.  

```python
ingredients = {"pasta", "tomatoes", "garlic", "basil",
               "olive oil", "pasta", "salt", "garlic"}

print(sorted(ingredients))
```

Also note that while defining a set if it contains duplicate values  
then it will remove duplicates automatically, no need to do anything extra.  

Creating a set  
Use curly braces and provide values separated by commas.  

```python
ingredients = {"pasta", "tomatoes", "garlic", "basil", "olive oil", "salt"}
```

We can use the built-in function `set()` to convert another data structure to a set.  
This is called casting to a set and while doing this duplicate values are removed  
automatically.  
