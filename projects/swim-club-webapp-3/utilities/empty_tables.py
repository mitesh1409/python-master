import sqlite3

SWIMCLUB_DB = "swimclub.db"

# Empty the swimmers, events, times tables
with sqlite3.connect(SWIMCLUB_DB) as dbc:
    db_cursor = dbc.cursor()
    db_cursor.execute("delete from swimmers")
    db_cursor.execute("delete from events")
    db_cursor.execute("delete from times")

print("swimmers, events & times tables are emptied.")
