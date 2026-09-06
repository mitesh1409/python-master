import statistics
from flask import Flask, session, render_template, request

import data_access
import swimclub
import hfpy_utils

app = Flask(__name__)
app.secret_key = "ABCD-5678-WXYZ"

@app.get("/")
def index():
    return render_template(
        "index.html",
        title="Welcome to Swimclub"
    )

@app.get("/swims")
def display_swim_sessions():
    data = data_access.get_swim_sessions()
    sessions = [value[0].split(" ")[0] for value in data]
    return render_template(
        "sessions.html",
        title="Select a swim session",
        select_id="session_date",
        sessions=sessions,
        url="/swimmers"
    )

@app.post("/swimmers")
def display_swimmers():
    session["session_date"] = request.form["session_date"]

    data = data_access.get_swimmers_by_session(session["session_date"])
    swimmers = [f"{value[0]}-{value[1]}" for value in data]

    return render_template(
        "swimmers.html",
        title="Select a swimmer",
        select_id="swimmer",
        swimmers=swimmers,
        url="/events"
    )

@app.post("/events")
def display_events():
    session["swimmer"], session["age"] = request.form["swimmer"].split("-")

    data = data_access.get_swimmers_events_by_session(session["swimmer"], session["age"], session["session_date"])
    events = [f"{value[0]} {value[1]}" for value in data]

    return render_template(
        "events.html",
        title="Select an event",
        select_id="event",
        events=events,
        url="/charts"
    )

@app.post("/charts")
def display_charts():
    distance, stroke = request.form["event"].split(" ")

    data = data_access.get_swimmers_times_by_event_and_session(session["swimmer"], session["age"], distance, stroke, session["session_date"])
    times = [value[0] for value in data]

    title = f"{session["swimmer"]} (Under {session["age"]}) {distance} {stroke} - {session["session_date"]}"

    time_values = [swimclub.time_to_hundredths_seconds(value) for value in times]

    average = swimclub.time_to_minutes_seconds_hundredths(statistics.mean(time_values))

    max_time_value = max(time_values)
    bar_values = []
    times.reverse()
    time_values.reverse()
    for n, time in enumerate(times):
        bar_values.append((
            hfpy_utils.convert2range(time_values[n], 0, max_time_value, 0, 400),
            time
        ))

    # Get the name of event from data file.
    event = swimclub.event_lookup(distance, stroke)

    # Get world records for this event.
    event_records = swimclub.event_records(event)

    return render_template(
        "barchart.html",
        title=title,
        average=average,
        bar_values=bar_values,
        event=event,
        event_records=event_records
    )

if __name__ == "__main__":
    app.run(debug=False, port=5001)
