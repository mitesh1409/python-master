# Print Floats

```python
# Print floats 1, 2, and 3
print(float1)
print(float2)
print(float3)

# Print floats 2 and 3 using the f string formatter
print(f"{float2:f}")
print(f"{float3:f}")

# Print float 3 with a 7 f string precision
print(f"{float3:.7f}")
```

Without format specifier floats are displayed up to 4 decimal places.  

If a float value has more than 4 decimal places then without any format specifier  
it will be displayed in scientific notation.  

Format specifier "f" displays up to 6 decimal places only.  
