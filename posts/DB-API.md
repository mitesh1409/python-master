# Python DB-API

The Python DB-API provides a number of methods  
for interacting with your chosen database engine,  
including `execute`, `fetchall`, `fetchmany`, and `fetchone`.

The `execute` method sends an SQL query/statement  
to your chosen database engine.

The `fetchall` method returns results as a list of  
tuples (when at least one row is returned) or an  
empty list (when no results are returned from your  
database engine).

The `fetchmany` method operates like `fetchall`, but  
for the fact that you can specify a maximum number  
of rows to return. Repeated calls to `fetchmany`  
allows you to implement pagination (should you need it).

The `fetchone` method returns one, and only one,  
tuple of results from your database engine. Like with  
`fetchall` and `fetchmany`, the results can be empty.
