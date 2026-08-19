# `__pycache__` folder

That folder is used internally by the Python interpreter to save cached compiled copies  
of any modules you create and then import.  

Although you don’t have to compile your Python code to run it, behind the scenes Python  
converts your code to an internal bytecode, which is then executed.  

As this process can sometimes be expensive when importing modules, the interpreter caches  
a copy of the compiled bytecode in the "__pycache__" folder during the import process.  

The next time you import your module (in a new session), the interpreter checks your  
module’s timestamp against the timestamp of the cached bytecode and, if they are the same,  
reuses the bytecode. Otherwise, the code to bytecode process starts all over again.  

You can safely ignore any files in the __pycache__ folder and leave everything to the  
interpreter to manage (although you might want to exclude the folder from your Git repo).  
