# Dictionaries

```python
# Creating a dictionary
recipe = {"pasta": 500,
          "tomatoes": 400,
          "garlic": 15,
          "basil": 20,
          "olive oil": 30,
          "salt": 5}

print(recipe) # Whole dictionary
print(recipe.keys()) # Gets all keys.
print(recipe.values()) # Gets all values.
print(recipe.items()) # Gets all the items as a list of tuples, where each tuple contains key-value pair.
```

Dictionaries do not accept duplicate keys,  
in case we have duplicate keys then the most  
recent key will overwrite earlier value.  

Duplicate keys will overwrite previous values without error.  
So keep this in mind while debugging dictionaries.  

Please note that when you print dictionary it will not show duplicate keys.  

```python
recipe = {"pasta": 500,
          "tomatoes": 400,
          "garlic": 15,
          "basil": 20,
          "olive oil": 30,
          "garlic": 25,
          "salt": 5}

print(recipe["garlic"]) # It will be 25 not 15.

print(recipe) # Please note that when you print dictionary it will not show duplicate keys.
```

Creating a dictionary  
Use curly braces and provide key-value pairs separated by commas.  

```python
recipe = {"pasta": 500,
          "tomatoes": 400,
          "garlic": 15,
          "basil": 20,
          "olive oil": 30,
          "garlic": 25,
          "salt": 5}
```

---

We can convert a list of dictionaries to pandas DataFrame to facilitate data analysis.  

```python
import pandas as pd

...

df = pd.DataFrame(list_of_dicts)
print(df.head())
```

---

Key points:  

* **Creating dictionaries**: You discovered two methods for creating dictionaries: using the `dict()` method and the curly braces `{}`. For example, `art_galleries = {}` initializes an empty dictionary.

* **Accessing and adding data**: You learned how to add data to dictionaries and access existing data. This involves assigning values to keys and using keys to retrieve values.

* **Looping through dictionaries**: The lesson showed you how to iterate over dictionaries, including looping over keys, values, and key-value pairs (items). This is crucial for processing each element in a dictionary.

* **Handling missing keys**: You explored how to safely access dictionary values using the `.get()` method to avoid KeyError exceptions when a key is not found. This method allows for a default value to be returned if the key doesn't exist.
