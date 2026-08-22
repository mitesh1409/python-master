import statistics
import hfpy_utils

__all__ = ["process_swim_data", "generate_bar_chart"]

# File location
DATA_FOLDER = "swimdata"

# Charts location
CHARTS_FOLDER = "charts"

def _time_to_hundredths_seconds(time_str):
    parts = time_str.split(":")
    if len(parts) == 2:
        minutes, rest = parts
    else:
        minutes = 0
        rest = parts[0]

    parts = rest.split(".")
    if len(parts) == 2:
        seconds, hundredths = parts
    else:
        seconds = parts[0]
        hundredths = 0

    total_hundredths = (int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths)
    return total_hundredths

def _time_to_minutes_seconds_hundredths(time_value):
    mins_secs, hundredths = f"{(time_value / 100):.2f}".split(".")
    mins_secs = int(mins_secs)
    mins = mins_secs // 60
    secs = mins_secs - (mins * 60)
    return f'{mins}:{secs:0>2}.{hundredths}'

def process_swim_data(filename):
    # Extracting data from the filename.
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")

    # Reading data from the file
    with open(f"{DATA_FOLDER}/{filename}") as file:
        lines = file.readlines()

    # We have only one line of data, getting time entries from it.
    times = lines[0].strip().split(",")

    time_values = []
    for t in times:
        value = _time_to_hundredths_seconds(t)
        time_values.append(value)

    average_time = _time_to_minutes_seconds_hundredths(statistics.mean(time_values))

    return swimmer, age, distance, stroke, times, average_time, time_values

def generate_bar_chart(filename):
    # Process file data
    swimmer, age, distance, stroke, times, average, time_values = process_swim_data(filename)

    # Construct the title
    title = f"{swimmer} (Under {age}) {distance} {stroke}"

    # Construct SVG bars
    max_time_value = max(time_values)
    svg_bars = ""

    times.reverse()
    time_values.reverse()
    for n, t in enumerate(times):
        bar_width = hfpy_utils.convert2range(time_values[n], 0, max_time_value, 0, 400)

        svg_bar = f"""
        <svg height="30" width="450">
            <rect height="30" width="{bar_width}" style="fill:rgb(0,0,255);" />
        </svg>{t}<br />
        """

        svg_bars += svg_bar

    # File to save bar charts
    save_to = f"{CHARTS_FOLDER}/{filename.replace(".txt", ".html")}"

    # HTML + SVG content for the bar chart file
    html_page = f"""
    <!DOCTYPE html>
    <html>

    <head>
        <title>
            {title}
        </title>
    </head>

    <body>
        <h3>{title}</h3>

        {svg_bars}

        <p>Average time: {average}</p>
    </body>

    </html>
    """

    with open(save_to, "w") as tf:
        print(html_page, file=tf)

    return save_to
