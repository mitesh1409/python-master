# Virtual Environment

A virtual environment is a named clean installation of Python.  
Here “clean” means that the only things installed in your  
virtual environment are Python itself together with the PSL.  
The “named” bit refers to the fact that each virtual environment  
is assigned an individual name, and it should come as no surprise  
that you can have as many virtual environments on your computer  
as your disk space allows (and you can think up unique names for).

Now—and this is a key insight—if you install a package from PyPI  
into a virtual environment, it is only available in that named  
virtual environment. It’s not even available in the “main” Python  
installed on your computer. The virtual environment effectively hides  
and compartmentalizes a version of Python for you.  

As you might have already guessed, it’s often regarded as good  
practice to create a virtual environment for each of your Python  
projects. This then allows you to only install the packages your  
project needs, safe in the knowledge that you aren’t messing anything  
up for anything else. Why this is important becomes clear when you consider  
that a virtual environment can install any release/version of Python  
as well as any release/version of a PyPI package. So if you have a project  
that needs Flask v1 to run, and another project which needs Flask v2,  
simply pop each of your projects into their own virtual environment.  
This then gives you the flexibility to install whichever version  
of Flask into each environment as needed.
