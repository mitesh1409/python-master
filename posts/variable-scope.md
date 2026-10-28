# Variable Scope

Global Scope

Function Scope

```python
global_value = 99

def foo():
    # global global_value # this means you want to use global, you can read and update/modify it.
    global_value = 1 # local shadows global, this means you want to use local, global is not disturbed.
    local_value = global_value + 11
    print(f"local_value = {local_value}")
    print(f"global_value = {global_value}")

foo()

# Can't access local_value outside the function.
# print(f"local_value = {local_value}")

print(f"global_value = {global_value}")
```
