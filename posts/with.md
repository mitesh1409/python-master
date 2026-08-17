# `with` statement

You can call open directly in your code, opening a named file, processing its data,  
then closing the file when you’re done. This open-process-close pattern is very  
common, regardless of the programming language you use. In fact, Python has a  
language statement that makes working with the open-process-close pattern especially  
convenient: the `with` statement.

If you open your file with `with`, Python arranges to automatically close your file  
when you’re done, regardless of what happens during whatever processing you perform  
on the file. It will close the file even if your code raises an exception or code crashes.  
This is a very useful feature, because it means you don’t have to worry about closing the file yourself.  

The word `with` is a Python keyword that you’ll see used in lots  
of contexts: it not just for use with files. What `with` does is setup a  
context within which your code runs, and the code can have a set-up  
and teardown mechanism. For files, the setup is opening the file, and the  
teardown is closing it.  

Reference:  
Book: Head First Python 3rd Edition
