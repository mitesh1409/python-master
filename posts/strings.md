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

* Documentation.
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
