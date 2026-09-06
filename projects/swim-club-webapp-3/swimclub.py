import json

__all__ = [
    "time_to_hundredths_seconds",
    "time_to_minutes_seconds_hundredths",
    "event_lookup",
    "event_records"
]

def time_to_hundredths_seconds(time_str):
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

def time_to_minutes_seconds_hundredths(time_value):
    mins_secs, hundredths = f"{(time_value / 100):.2f}".split(".")
    mins_secs = int(mins_secs)
    mins = mins_secs // 60
    secs = mins_secs - (mins * 60)
    return f'{mins}:{secs:0>2}.{hundredths}'

def event_lookup(distance, stroke):
    conversions = {
        "Free": "freestyle",
        "Back": "backstroke",
        "Breast": "breaststroke",
        "Fly": "butterfly",
        "IM": "individual medley",
    }

    return f"{distance} {conversions[stroke]}"

def event_records(event):
    world_records = {}
    with open("swimming_world_records.json", "r") as wr_file:
        world_records = json.load(wr_file)

    return {
        "lc_men": world_records["LC Men"][event],
        "sc_men": world_records["SC Men"][event],
        "lc_women": world_records["LC Women"][event],
        "sc_women": world_records["SC Women"][event],
    }
