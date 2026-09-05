import sqlite3
import os

SWIMCLUB_DATA_FOLDER = "swimdata"
SWIMCLUB_DB = "swimclub.db"

data_files = os.listdir(SWIMCLUB_DATA_FOLDER)

if ".DS_Store" in data_files:
    data_files.remove(".DS_Store")

swimmers = []
events = []

for data_file in data_files:
    name, age, distance, stroke = data_file.removesuffix(".txt").split("-")
    if (name, age) not in swimmers:
        swimmers.append((name, age))
    if (distance, stroke) not in events:
        events.append((distance, stroke))

populate_swimmers_query = """
    insert into swimmers
    (name, age)
    values
    (?, ?)
"""

populate_events_query = """
    insert into events
    (distance, stroke)
    values
    (?, ?)
"""

# Populate swimmers and events data.
with sqlite3.connect(SWIMCLUB_DB) as dbc:
    db_cursor = dbc.cursor()
    db_cursor.executemany(populate_swimmers_query, swimmers)
    db_cursor.executemany(populate_events_query, events)

populate_times_query = """
    insert into times
    (swimmer_id, event_id, time)
    values
    (?, ?, ?)
"""

# Populate times data.
with sqlite3.connect(SWIMCLUB_DB) as dbc:
    db_cursor = dbc.cursor()
    for data_file in data_files:
        name, age, distance, stroke = data_file.removesuffix(".txt").split("-")
        swimmer_id = db_cursor.execute("select id from swimmers where name = ? and age = ?", (name, age)).fetchone()[0]
        event_id = db_cursor.execute("select id from events where distance = ? and stroke = ?", (distance, stroke)).fetchone()[0]
        with open(f"swimdata/{data_file}", "r") as fs:
            data = fs.readlines()[0]
            times = data.strip().split(",")
            times = list(map(lambda value: (swimmer_id, event_id, value.strip()), times))
            db_cursor.executemany(populate_times_query, times)

print("swimmers, events & times tables are populated with data successfully!")

# Verification of inserted data
with sqlite3.connect(SWIMCLUB_DB) as dbc:
    db_cursor = dbc.cursor()
    swimmers_count = db_cursor.execute("select count(*) from swimmers").fetchone()[0]
    events_count = db_cursor.execute("select count(*) from events").fetchone()[0]
    times_count = db_cursor.execute("select count(*) from times").fetchone()[0]

print(f"{swimmers_count} Swimmers")
print(f"{events_count} Events")
print(f"{times_count} Times")
