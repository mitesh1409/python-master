# Strings

String values are always quoted, either using single quotes `''` or double quotes `""`.  

For multiline strings there is a convention to use 3 sets of double quotes `"""`.  
This approach enhances readability.  

```python
# Create a string variable over multiple lines
recipe_instructions = """1. Bring a large pot of salted water to boil and cook pasta
2. Heat olive oil in a pan and sauté minced garlic until fragrant
3. Add chopped tomatoes and simmer for 10 minutes
4. Toss cooked pasta with tomato sauce and fresh basil leaves
"""
```

Where Multiline Strings used?  

* Documentation/Multi-line Comments.
* Longer text such as instructions or error messages.

---

In case of strings,  
`+` will do concatenation.  
`*` will do repeatation.  
Other operators will result in an error.  

```python
greetings = "Hello"
user_fname = "Mitesh"

print(greetings + " " + user_fname) # Hello Mitesh

print(greetings * 3) # HelloHelloHello
```

---

Strings are evaluated in alphabetical order.  

```python
"James" > "Brian" # True

"Apple" > "Banana" # False
```

---

```bash
>>> import string
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> 
>>> string.digits
'0123456789'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> 
```

These can be used in string validations.  

---

Reversing a string is easy with `hello[::-1]`.   

```bash
>>> hello = 'Hello'
>>>
>>>
>>> hello[:]
'Hello'
>>>
>>> hello[::1]
'Hello'
>>>
>>>
>>> hello[::2]
'Hlo'
>>>
>>>
>>> hello[::-1]
'olleH'
>>>
>>>
>>> hello[::-2]
'olH'
>>>
>>>
```

---

Problem statement: You can only pass max 50 words, for more than that buy "Pro" plan.

How to count words in a string?  

1. strip input string to remove white spaces at the start and end.
2. Count spaces in a string.
3. No. of words = no. of spaces + 1

```bash

>>> input_str = "  Hello! How are you?  "
>>>
>>>
>>> input_str.count(" ")
7
>>>
>>>
>>> input_str.strip()
'Hello! How are you?'
>>>
>>> input_str
'  Hello! How are you?  '
>>>
>>>
>>>
>>> input_str.strip().count(" ")
3
>>>
>>>

```

But this is not accurate as we can have multiple spaces in between the words.  
Then it will give incorrect word count.

So correct approach is to use `split()` method of a string.

```bash

>>> input_str
'  Hello! How are you?  '
>>>
>>>
>>> input_str.split()
['Hello!', 'How', 'are', 'you?']
>>>
>>>
>>> items = input_str.split()
>>> len(items)
4
>>>
>>>
>>> input_str = "  Hello!  How  are  you?  "
>>>
>>> items = input_str.split()
>>> len(items)
4
>>>

```
