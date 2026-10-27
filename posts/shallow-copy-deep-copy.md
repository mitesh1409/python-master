# Shallow Copy, Deep Copy

```python

# 1
list_one = [1, 2, 3]
print(list_one)
print(id(list_one))

list_two = list_one.copy()
print(list_two)
print(id(list_two))

# 2
list_one = [[11, 22, 33], [44, 55, 66]]
print(list_one)
print(id(list_one))

list_two = list_one.copy()
print(list_two)
print(id(list_two))

# 3
list_one = [[11, 22, 33], [44, 55, 66]]
print(list_one)
print(id(list_one))

print('\n')

list_two = list_one.copy()
print(list_two)
print(id(list_two))

print('\n')

list_one[0].append(123)

print(list_two)
print(id(list_two))

```

In #3 above, when we do copy of `list_one` and save it into `list_two`,  
`list_two` has a shallow copy of `list_one`, meaning `list_two` just copies  
references to inner/nested lists `[11, 22, 33]` & `[44, 55, 66]`.  

That is why when we change the first list  
`list_one[0].append(123)`  
it is also reflected in `list_two`.  


How to Deep Copy?


```python

# 4
import copy

list_one = [[11, 22, 33], [44, 55, 66]]
print('List One')
print(list_one)
print(id(list_one))
print('\n')

list_two = copy.deepcopy(list_one)
print('List Two')
print(list_two)
print(id(list_two))
print('\n')

list_one[0].append(123)

print('After appending')
print('\n')

print('List One')
print(list_one)
print(id(list_one))
print('\n')

print('List Two')
print(list_two)
print(id(list_two))
print('\n')

```
