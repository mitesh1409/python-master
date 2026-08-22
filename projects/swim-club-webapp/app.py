from flask import Flask, session, render_template, request
import os

import swimclub

app = Flask(__name__)
app.secret_key = "ABCD-5678-WXYZ"

def load_session():
    if "swimmers" not in session:
        session["swimmers"] = swimclub.get_swimmers()

@app.get("/")
def index():
    return render_template(
        "index.html",
        title="Welcome to the Swimclub system"
    )

@app.get("/swimmers")
def display_swimmers():
    load_session()
    swimmers = sorted(list(session["swimmers"].keys()))
    return render_template(
        "select.html",
        title="Select a swimmer",
        select_id="swimmer",
        data=swimmers,
        url="/showfiles"
    )

@app.post("/showfiles")
def display_swimmers_files():
    load_session()
    name = request.form["swimmer"]
    return render_template(
        "select.html",
        title="Select an event",
        select_id="file",
        data=session["swimmers"][name],
        url="/showbarchart"
    )

@app.post("/showbarchart")
def show_bar_chart():
    file_id = request.form["file"]
    location = swimclub.generate_bar_chart(file_id, "templates")
    return render_template(location.split("/")[1])

if __name__ == "__main__":
    app.run(debug=False)
