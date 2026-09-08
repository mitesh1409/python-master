# Type Hints

Type hints allow you to add an *optional* notation to your function signatures to  
hint at the argument types expected, as well as specify your function’s return type.  

Some third-party developer tools (with PyPI’s `mypy` being the most famous) can  
preprocess your code to ensure the calls to your functions conform to their type  
hinted signature, complaining loudly when an infraction is spotted. This can be  
useful to know.

Critically, Python ignores all type hints. If you send a dictionary to a function  
expecting a string, Python happily accepts it, sends the dictionary to your function  
then—like everyone else—crosses its fingers and hopes for the best. There’s no  
mechanism built in to Python to check a call against your type hints (and there  
likely never will be). Type hints are optional, after all.  
