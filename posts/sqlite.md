# SQLite

Most Widely Deployed and Used Database Engine  
https://www.sqlite.org/mostdeployed.html

SQLite comes built in to Python.  
https://docs.python.org/3/library/sqlite3.html

---

Python ships with `sqlite3` as part of its **standard library** — no installation needed.

```python
import sqlite3  # ✅ works out of the box, no pip install required
```

**Quick overview of what you can do with it:**

```python
import sqlite3

# Connect to a database (creates the file if it doesn't exist)
conn = sqlite3.connect('mydb.db')

# Create a cursor to execute SQL
cursor = conn.cursor()

# Execute SQL
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Mitesh", 42))

# Commit and close
conn.commit()
conn.close()
```

---

**Key points:**

- SQLite stores the entire database in a **single `.db` file**
- No separate database server needed — unlike PostgreSQL or MySQL
- Perfect for small apps, local tools, prototypes, and learning
- The `sqlite3` module is part of Python's standard library — same as `os`, `sys`, `math` etc.

> 💡 For your small app or app in MVP phase, SQLite is a great fit, there is no need for a heavy database server.

---

```sqlite
pragma table_list

pragma table_info(<table-name>)
```

---

SQLite is a single-process, file-based, database  
management engine that requires very little admin  
to run. All of your interactions with the engine can be  
executed from within Python code. This makes using  
SQLite an excellent choice when starting out, as you  
can experiment with ease.
