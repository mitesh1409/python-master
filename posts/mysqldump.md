# mysqldump

The mysqldump command (included with MySQL/MariaDB) lets you create a  
copy of not just the data contained in any database, but also its table definitions.  
The file produced contains both the database table definitions and the data.  

A typical use of  
“mysqldump” is to  
create backups of  
running databases.  

For example:  

Run the following command from where you want to take database dump.  
Run this on MySQL CLI from local environment.  

`sudo mysqldump swimdb > db.sql`

Where "swimdb" is the database name.  
This takes full dump (table definitions/schemas + data) of the "swimdb" database.

Then run the following command where you want to setup database.  
`source db.sql`
