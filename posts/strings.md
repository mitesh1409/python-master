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

---

Stride

String slicing also accepts a third index which specifies how many characters to omit before retrieving a character. In the example, the specified indices returns the following output. They are the characters retrieved between positions zero and six, skipping two characters in between. Interestingly, omitting the first and second indices and designating a minus one step returns a reversed string as shown in the output.

In python, you can also specify steps by using a third index. If you don't specify the first or second index and the third one is negative, it will return the characters jumping and backward.

---

Get the palindrome by reversing the string contained in movie_title.

A palindrome string is a sequence of characters that reads the same forward and backward.

**Common Ways to Check a Palindrome**  

* Two-pointer comparison (O(n) time, O(1) space): Compare characters from the start and end moving inward toward the center. Most developers on Stack Overflow agree on iterating from both ends inward to compare symmetrical characters.

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

* Reverse and compare (O(n) time, O(n) space): Reverse the string and check if it equals the original (as covered in GeeksforGeeks' Palindrome String guide).

```python

movie_title = 'The Fall'

print(movie_title)

# Palindrome of a string
reversed_movie_title = movie_title[::-1]
print(reversed_movie_title)

if movie_title == reversed_movie_title:
    print(f'{movie_title} is palindrome.')

```

---

**Replacing negations**  

In order to keep working with your prediction project, your next task is to figure out how to handle negations that occur in your dataset. Some algorithms for prediction do not work well with negations, so a good way to handle this is to remove either not or n't, and to replace the next word by its antonym.

Let's imagine that you have the string: The movie isn't good. You will need to remove n't and replace good for bad. This way, your string ends up being The movie is bad. You notice that in the first column of the dataset, you have a string that uses the word isn't followed by important.

The text of this column has been already saved in the variable movies so you start working with it. You can use print(movies) to view it in the IPython Shell.

```python
# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)
```

---

String formatting = String interpolation

Methods of string formatting

* Positional formatting
* Formatted string literals or f-strings
* Template method

#1 Positional formatting

```python

text = "Machine learning provides {} the ability to learn {}."

print(text.format("systems", "automatically"))

```

Ouput

```
Machine learning provides systems the ability to learn automatically.
```

#2 Formatted string literals or f-strings

#3 Template method

