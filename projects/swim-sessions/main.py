import statistics

def main():
    # Filename and location
    FOLDER = "swimdata"
    FILENAME = "Darius-13-100m-Fly.txt"

    # Extracting data from the filename.
    swimmer, age, distance, stroke = FILENAME.removesuffix(".txt").split("-")

    # Reading data from the file
    with open(f"{FOLDER}/{FILENAME}") as file:
        lines = file.readlines()

    # We have only one line of data, getting time entries from it.
    times = lines[0].strip().split(",")

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

    time_values = []
    for t in times:
        value = time_to_hundredths_seconds(t)
        time_values.append(value)

    def time_to_minutes_seconds_hundredths(value):
        mins_secs, hundredths = str(round(value / 100, 2)).split(".")
        mins_secs = int(mins_secs)
        mins = mins_secs // 60
        secs = mins_secs - (mins * 60)
        return f'{mins}:{secs}.{hundredths}'

    average_time = time_to_minutes_seconds_hundredths(statistics.mean(time_values))

    print(f"Swimmer: {swimmer}, Age: {age}, Distance: {distance}, Stroke: {stroke}\n")

    print("=" * 20)
    print("\n\n")

    print("Timings\n")
    print("-" * 20)

    for t in times:
        print(t + "\n")

    print("=" * 20)
    print("\n\n")

    print(f"Average Time: {average_time}")

if __name__ == "__main__":
    main()
