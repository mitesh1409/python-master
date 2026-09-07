import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

import queries

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

def get_swim_sessions():
    with engine.connect() as conn:
        sessions = conn.execute(text(queries.SQL_SESSIONS)).fetchall()
    return sessions

def get_swimmers_by_session(date):
    with engine.connect() as conn:
        swimmers = conn.execute(
            text(queries.SQL_SWIMMERS_BY_SESSION),
            {"date": date}
        ).fetchall()
    return swimmers

def get_swimmers_events_by_session(name, age, date):
    with engine.connect() as conn:
        events = conn.execute(
            text(queries.SQL_SWIMMERS_EVENTS_BY_SESSION),
            {"name": name, "age": age, "date": date}
        ).fetchall()
    return events

def get_swimmers_times_by_event_and_session(name, age, distance, stroke, date):
    with engine.connect() as conn:
        times = conn.execute(
            text(queries.SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION),
            {"name": name, "age": age, "distance": distance, "stroke": stroke, "date": date}
        ).fetchall()
    return times