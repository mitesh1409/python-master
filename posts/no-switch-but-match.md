# No Switch but Match

A common question when programmers first encounter Python is to ask: Does Python  
have a switch statement? For close to thirty years, every Python programmer answered  
in the negative, then pointed to a multiway if statement (which sort of does the same thing):  

No switch/match

```python
thing = "a"

if thing == 1:
    print("You look like 1.")
elif thing == "A":
    print("You look like A.")
elif thing == "B":
    print("You look like B.")
elif thing == "a":
    print("You look like a.")
else:
    print("We've no idea what you are.")
```

The release of Python 3.10 changed everything, with the addition of the match  
statement to the language. We still don’t have a switch, but who needs one of those  
when you’ve got match? Take a look:  

```python
thing = "A"

match thing:
    case 1:
        print("You look like 1.")
    case "A":
        print("You look like A.")
    case "B":
        print("You look like B.")
    case "a":
        print("You look like a.")
    case _:
        print("We've no idea what you are.")
```
