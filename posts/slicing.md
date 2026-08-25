# Slicing a sequence of data

You can ask Python to copy a slice from any sequence. As lists and strings are both  
sequences, they support the slice notation. When you slice a sequence, you get back  
a copy of the sliced data. The original data remains unchanged.

```python
nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Returns a copy of the first 5 numbers from the list.
nums[:5] # [0, 10, 20, 30, 40]

# The original list remains unchanged.
nums # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

msg = "My name is Mitesh, and I'm doing good. How about you?"

# Returns a copy of the first 10 characters from the string.
msg[:10] # My name is

# The original string remains unchanged.
msg # My name is Mitesh, and I'm doing good. How about you?
```

A slice lets you extract a sequential portion of any sequence. You specify  
where the portion starts and stops within the square brackets.

Starting index is inclusive.  
Stoping index is exclusive.  

```python
nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Starts at index 1, Stops at index 5 (index 5 is exclusive)
nums[1:5]

fav = "Life, the Universe and Everything."

fav[10:18] # Universe
fav[23:33] # Everything
fav[23:-1] # Everything
```

The length of the slice is = stop index - start index.

The start and stop values have defaults  

If you exclude the start value, it is assumed to be zero (the start of the  sequence).  
Excluding the stop value extends the slice to the end of the current sequence.  

In the following example the start value defaults to zero.  

```python
fav = "Life, the Universe and Everything."

fav[:4] # Life
```

In the following we are using negative index values.  

```python
fav = "Life, the Universe and Everything."

fav[-11:-1] # Everything (. not there since it is at -1 index)
fav[-11:] # Everything.
fav[23:] # Everything.
```

Relying on the default values for start and stop doesn’t always makes sense.  

```python
fav = "Life, the Universe and Everything."

# Looks confusing at first sight.
fav[:] # Life, the Universe and Everything.

# It looks clear.
fav # Life, the Universe and Everything.
```

An optional third number can be added to your  
slice specification. Called step, it indicates  
the frequency of the slice extraction from any  
sequence.

Here’s the general slice form:  
[ start : stop : step ]

The best way to describe step is with a few  
examples:

```python
fav = "Life, the Universe and Everything."

fav # Life, the Universe and Everything.
fav[::2] # Lf,teUies n vrtig
fav[::3] # Let ir dvyi.
fav[::-1] # .gnihtyrevE dna esrevinU eht ,efiL
```
