from flask import Flask, session, render_template, request

import swimclub
import hfpy_utils

app = Flask(__name__)
app.secret_key = "ABCD-5678-WXYZ"

def load_session():
    if "swimmers" not in session:
        session["swimmers"] = swimclub.get_swimmers()

@app.get("/")
def index():
    return render_template(
        "index.html",
        title="Welcome to Swimclub"
    )

@app.get("/swimmers")
def display_swimmers():
    load_session()
    swimmers = sorted(list(session["swimmers"].keys()))
    return render_template(
        "swimmers.html",
        title="Select a swimmer",
        select_id="swimmer",
        swimmers=swimmers,
        url="/events"
    )

@app.post("/events")
def display_events():
    load_session()
    name = request.form["swimmer"]
    return render_template(
        "events.html",
        title="Select an event",
        select_id="event",
        files=session["swimmers"][name],
        url="/charts"
    )

@app.post("/charts")
def display_charts():
    file_id = request.form["event"]
    swimmer, age, distance, stroke, times, average, time_values = swimclub.process_swim_data(file_id)

    title = f"{swimmer} (Under {age}) {distance} {stroke}"

    max_time_value = max(time_values)
    bar_values = []
    times.reverse()
    time_values.reverse()
    for n, time in enumerate(times):
        bar_values.append((
            hfpy_utils.convert2range(time_values[n], 0, max_time_value, 0, 400),
            time
        ))

    return render_template(
        "barchart.html",
        title=title,
        average=average,
        bar_values=bar_values
    )

if __name__ == "__main__":
    app.run(debug=False)
