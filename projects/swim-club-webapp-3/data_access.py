import sqlite3
import queries

# SWIMCLUB_DB = "swimclub.db"
SWIMCLUB_DB = "CoachDB.sqlite3"

def get_swim_sessions():
    with sqlite3.connect(SWIMCLUB_DB) as dbc:
        db_cursor = dbc.cursor()
        sessions = db_cursor.execute(queries.SQL_SESSIONS).fetchall()
    return sessions

def get_swimmers_by_session(date):
    with sqlite3.connect(SWIMCLUB_DB) as dbc:
        db_cursor = dbc.cursor()
        swimmers = db_cursor.execute(queries.SQL_SWIMMERS_BY_SESSION, (date,)).fetchall()
    return swimmers

def get_swimmers_events_by_session(name, age_group, date):
    with sqlite3.connect(SWIMCLUB_DB) as dbc:
        db_cursor = dbc.cursor()
        events = db_cursor.execute(queries.SQL_SWIMMERS_EVENTS_BY_SESSION, (name, age_group, date)).fetchall()
    return events

def get_swimmers_times_by_event_and_session(name, age_group, distance, stroke, date):
    with sqlite3.connect(SWIMCLUB_DB) as dbc:
        db_cursor = dbc.cursor()
        times = db_cursor.execute(queries.SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION, (name, age_group, distance, stroke, date)).fetchall()
    return times
