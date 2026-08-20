# list-set-list -> removes duplicates -> gives unique values

Example

```python
# Lets assume we are developing an app for the swim club.

# A list of 60 swimmers, but there are duplicate entries in this list.
swimmers = ['Abi', 'Abi', 'Abi', 'Abi', 'Abi', 'Ali', 'Ali', 'Alison', 'Alison', 'Aurora', 'Bill', 'Bill', 'Blake', 'Blake', 'Blake', 'Calvin', 'Calvin', 'Calvin', 'Carl', 'Chris', 'Chris', 'Darius', 'Darius', 'Darius', 'Darius', 'Dave', 'Dave', 'Elba', 'Emma', 'Emma', 'Erika', 'Erika', 'Erika', 'Hannah', 'Hannah', 'Katie', 'Katie', 'Katie', 'Katie', 'Katie', 'Katie', 'Katie', 'Lizzie', 'Lizzie', 'Maria', 'Mike', 'Mike', 'Mike', 'Mike', 'Mike', 'Owen', 'Ruth', 'Ruth', 'Ruth', 'Ruth', 'Ruth', 'Tasmin', 'Tasmin', 'Tasmin', 'Tasmin']

# How do we get unique swimmers?

# Lets convert the above list into a set.
# A set will remove duplicates automatically.
set(swimmers)

# Getting back to the list.
# Now convert the set into a list.
# This list now contains unique values.
unique_swimmers = list(set(swimmers))
```
