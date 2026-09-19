import sqlite3

SWIMCLUB_DB = "swimclub.db"

create_swimmers_table = """
    create table if not exists swimmers (
        id integer not null primary key autoincrement,
        name varchar(32) not null,
        age integer not null
    )
"""

create_events_table = """
    create table if not exists events (
        id integer not null primary key autoincrement,
        distance varchar(16) not null,
        stroke varchar(16) not null
    )
"""

create_times_table = """
    create table if not exists times (
        id integer not null primary key autoincrement,
        swimmer_id integer not null,
        event_id integer not null,
        time varchar(16) not null,
        created_at timestamp default current_timestamp
    )
"""

with sqlite3.connect(SWIMCLUB_DB) as dbc:
    db_cursor = dbc.cursor()
    db_cursor.execute(create_swimmers_table)
    db_cursor.execute(create_events_table)
    db_cursor.execute(create_times_table)
    results = db_cursor.execute("pragma table_list")

print(results.fetchall())
print(f"Database {SWIMCLUB_DB} created successfully.")
print("swimmers, events and times tables are created successfully!")

# ```sql
# CREATE USER 'swimDB_admin'@'localhost' IDENTIFIED BY 'password';
# GRANT ALL ON swimDB.* TO 'swimDB_admin'@'localhost';
# FLUSH PRIVILEGES;
# ```
