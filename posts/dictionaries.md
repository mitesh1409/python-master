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
