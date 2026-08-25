# Web Scraping

As with most other technologies in the Python space, there is more than one way  
to grab data off the internet.

The classic technique involves using the most-downloaded third-party Python package  
from PyPI, called **requests**, which is often twinned with another classic HTMLparsing  
technology, called **Beautiful Soup** (and known the world over as **bs4**). To parse  
HTML effectively, **bs4** needs to employ the services of a third-party parsing engine,  
with **lxml** a popular choice (although there are others).  

If you’ve been paying attention (and counting) we’re up to three potential package  
installs from PyPI (**requests**, **bs4**, and **lxml**). Although these three PyPI  
packages have excellent (and well-deserved) reputations, it would be nicer if a single  
package could do enough to handle all of our needs here.

The **gazpacho** package (also on PyPI) is designed to make web scraping as simple as  
possible. It may not be as powerful as the **requests**/**bs4**/**lxml** combo but it  
is good to get started.  

Gazpacho is a cold soup, popular in Spain and  
Portugal. gazpacho is a Python library that parses  
HTML, which it refers to as “soup.”

“gazpacho” is the  
name given to a tasty  
Spanish soup, which is  
served *cold* !!!

What’s with all  
the references  
to “soup”?!?  

That’s a tasty question...  

Using the word “soup” to refer to HTML-parsing  
technologies may strike you as odd.  
This is gazpacho’s way of paying homage to the  
grandparent of all Python HTML-processing libraries:  
Beautiful Soup. When used with requests, Beautiful  
Soup is a potent tool. As you can tell from the name,  
Beautiful Soup established the practice of referring to  
parsed HTML as “soup,” and it’s a convention that’s stuck.
