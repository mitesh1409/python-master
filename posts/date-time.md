# DateTime & Timezones in Python

## Built-in `datetime` module

```python
from datetime import datetime, timezone, timedelta

# Naive datetime — no timezone (avoid in production)
dt = datetime(2026, 9, 24, 11, 34, 55)
print(dt.tzinfo)  # None

# Aware datetime — always prefer this
dt_utc = datetime.now(timezone.utc)
print(dt_utc.isoformat())  # '2026-09-24T11:34:55+00:00'
```

---

## `zoneinfo` — built-in timezone database (Python 3.9+)

```python
from zoneinfo import ZoneInfo
from datetime import datetime

dt = datetime.now(ZoneInfo("Europe/London"))
dt = datetime.now(ZoneInfo("Asia/Kolkata"))   # IST
dt = datetime.now(ZoneInfo("America/New_York"))
```

---

## `dateutil` — 3rd party, more powerful

```python
from dateutil import tz
from datetime import datetime

# Timezone handling
london = tz.gettz("Europe/London")
ist    = tz.gettz("Asia/Kolkata")

dt = datetime.now(tz.UTC)

# Convert between timezones
dt_london = dt.astimezone(london)
dt_ist    = dt.astimezone(ist)

# Parse any date string automatically
from dateutil.parser import parse
parse("24 Sep 2026")           # '2026-09-24 00:00:00'
parse("Sep 24, 2026 11:34 AM") # '2026-09-24 11:34:00'
parse("2026-09-24T11:34:55")   # ISO format
```

---

## Common operations

```python
from datetime import datetime, timezone, timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now(timezone.utc)

# Add/subtract time
tomorrow    = now + timedelta(days=1)
last_week   = now - timedelta(weeks=1)
next_month  = now + relativedelta(months=1)  # dateutil
next_year   = now + relativedelta(years=1)   # dateutil

# Format
now.strftime("%Y-%m-%d %H:%M:%S")  # '2026-09-24 11:34:55'
now.isoformat()                     # '2026-09-24T11:34:55+00:00'

# Parse from string
datetime.strptime("24-09-2026", "%d-%m-%Y")
```

---

## Industry standard practices

```python
# ✅ Always store/work in UTC
now_utc = datetime.now(timezone.utc)

# ✅ Convert to local timezone only for display
from zoneinfo import ZoneInfo
display_time = now_utc.astimezone(ZoneInfo("Asia/Kolkata"))

# ✅ Always use aware datetimes
datetime.now(timezone.utc)   # ✅ aware
datetime.now()               # ❌ naive — avoid

# ✅ Use ISO format for APIs and databases
now_utc.isoformat()  # '2026-09-24T11:34:55+00:00'
```

---

## `zoneinfo` vs `dateutil` — when to use which:

| | `zoneinfo` | `dateutil` |
|---|---|---|
| Built-in | ✅ Python 3.9+ | ❌ pip install |
| Timezone handling | ✅ | ✅ |
| Parse date strings | ❌ | ✅ |
| Relative deltas | ❌ | ✅ |
| Recommended for | Timezone conversion | Parsing + relative math |

---

> 💡 **Golden rule — UTC in, local out:**  
>
> - Always **store and compute** in UTC
> - Only **convert to local timezone** at the last moment for display
> - Never store local times in databases — DST changes will break your data

---

## `astimezone()` vs `replace()`

### `astimezone()` — converts datetime value to another timezone

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# Stored in DB as UTC
utc_time = datetime(2026, 9, 24, 6, 0, 0, tzinfo=timezone.utc)
print(utc_time)  # 2026-09-24 06:00:00+00:00

# Display to Indian user — value changes
ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))
print(ist_time)  # 2026-09-24 11:30:00+05:30  ← +5:30 added

# Display to UK user — value changes
uk_time = utc_time.astimezone(ZoneInfo("Europe/London"))
print(uk_time)   # 2026-09-24 07:00:00+01:00  ← +1 added
```

Same moment in time, different representations. ✅

---

### `replace()` — only changes the label, not the value

```python
from datetime import datetime, timezone

# Naive datetime — no timezone info
naive = datetime(2026, 9, 24, 11, 30, 0)
print(naive.tzinfo)  # None

# Just label it as UTC — value stays exactly the same
aware = naive.replace(tzinfo=timezone.utc)
print(aware)  # 2026-09-24 11:30:00+00:00  ← same time, just labelled
```

---

### When to use which — real world scenarios:

```python
# ✅ Use astimezone() — user display
# "Show this UTC timestamp in user's local timezone"
utc_time.astimezone(user_timezone)

# ✅ Use replace() — fixing naive datetimes
# "I know this naive datetime is UTC, just attach the label"
naive_from_db.replace(tzinfo=timezone.utc)

# ✅ Use replace() — legacy data migration
# "Old data has no timezone, we know it was stored in UTC"
old_record.replace(tzinfo=timezone.utc)
```

---

### Common mistake — using `replace()` when you should use `astimezone()`:

```python
utc_time = datetime(2026, 9, 24, 6, 0, 0, tzinfo=timezone.utc)

# ❌ Wrong — replace() just relabels, doesn't convert
wrong = utc_time.replace(tzinfo=ZoneInfo("Asia/Kolkata"))
print(wrong)  # 2026-09-24 06:00:00+05:30  ← wrong time!

# ✅ Correct — astimezone() properly converts
correct = utc_time.astimezone(ZoneInfo("Asia/Kolkata"))
print(correct)  # 2026-09-24 11:30:00+05:30  ← correct!
```

---

> 💡 **Simple mental model:**
>
> - `astimezone()` → **"What time is it there?"** — changes the clock value
> - `replace()` → **"This clock is in UTC"** — just adds a label, clock stays the same

---

> NOTE:  
> In general, whenever we really want to be sure of the duration between events  
> that might cross a daylight saving boundary, we need to do our math in UTC.  

---

Date difference gives a value of type "datetime.timedelta".

Subtracting dates/datetimes gives value of type "datetime.timedelta".

```python
# Import date
from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12, 13)

date_diff = end - start

print(date_diff) # 218 days, 0:00:00

print(type(date_diff)) # <class 'datetime.timedelta'>
```

---

```python
# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)

# Print the results in ISO 8601 format
print(dt.isoformat()) # 2017-10-01T15:26:26
```

Output  

```plaintext
2017-10-01T15:26:26
```

The **`T` is just a separator** between the date part and the time part in the ISO 8601 format. It stands for "Time".

```
2017-10-01T15:26:26
│          │
date       time
```

It has no value of its own. It simply marks where the date ends and the time begins.

---

**Why not use a space?**

A plain space (`2017-10-01 15:26:26`) is more readable for humans, but ISO 8601 uses `T` because:

- It gives a single token with no whitespace, so it is easy to parse and safe in URLs, filenames, JSON and CSV files
- It is unambiguous across systems and languages

---

**Changing the separator:**

`isoformat()` lets you choose it:

```python
from datetime import datetime

dt = datetime(2017, 10, 1, 15, 26, 26)

print(dt.isoformat())           # 2017-10-01T15:26:26
print(dt.isoformat(sep=" "))    # 2017-10-01 15:26:26
```

---

**Parsing it back:**

```python
dt = datetime.fromisoformat("2017-10-01T15:26:26")
```

---

**With a timezone, the full format looks like this:**

```python
from datetime import timezone

dt_utc = datetime(2017, 10, 1, 15, 26, 26, tzinfo=timezone.utc)
print(dt_utc.isoformat())  # 2017-10-01T15:26:26+00:00
```

You may also see a trailing `Z` (for example `2017-10-01T15:26:26Z`), which means UTC ("Zulu time").

---

> 💡 `T` separates date from time, and `Z` (or `+00:00`) marks UTC. Both are part of the ISO 8601 standard, which is what most APIs and databases use for timestamps.

---

**Turning strings into datetimes**  

When you download data from the Internet, dates and times usually come to you as strings. Often the first step is to turn those strings into datetime objects.

Reference  
%Y  -  4 digit year (0000-9999)
%m  -  2 digit month (1-12)
%d  -  2 digit day (1-31)
%H  -  2 digit hour (0-23)
%M  -  2 digit minute (0-59)
%S  -  2 digit second (0-59)

```python
# Import the datetime class
from datetime import datetime

# Starting string, in YYYY-MM-DD HH:MM:SS format
date_str = '2017-02-03 00:00:01'

# Write a format string to parse s
date_format = '%Y-%m-%d %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(date_str, date_format)

# Print d
print(d)
```

---

Daylight Saving

Clocks move forward in the Spring.

Clocks move backward in the Fall.

---

In general, whenever we really want to be sure of the duration between events  
that might cross a daylight saving boundary, we need to do our math in UTC.

---

Study the following example:  

**Cleaning daylight saving data with fold**  

As we've just discovered, there is a ride in our data set which is being messed up by a Daylight Savings shift. Let's clean up the data set so we actually have a correct minimum ride length. We can use the fact that we know the end of the ride happened after the beginning to fix up the duration messed up by the shift out of Daylight Savings.

Since Python does not handle tz.enfold() when doing arithmetic, we must put our datetime objects into UTC, where ambiguities have been resolved.

onebike_datetimes is already loaded and in the right timezone. tz and timezone have been imported. Use tz.UTC for the timezone.

```python
trip_durations = []
for trip in onebike_datetimes:
  # When the start is later than the end, set the fold to be 1
  if trip["start"] > trip["end"]:
    trip['end'] = tz.enfold(trip['end'], fold=1)
  # Convert to UTC
  start = trip['start'].astimezone(tz.UTC)
  end = trip['end'].astimezone(tz.UTC)

  # Subtract the difference
  trip_length_seconds = (end-start).total_seconds()
  trip_durations.append(trip_length_seconds)

# Take the shortest trip duration
print("Shortest trip: " + str(min(trip_durations)))
```

---

**Datacamp Project**  

You recently quit your job to start a space logistics company that uses rockets to deliver critical cargo to colonies on demand. Since you're still in the startup phase, you're handling everything yourself, including writing the software to manage complex scheduling and timing across different space colonies.

Before developing a full rocket flight planning and logistics system, you want to create core functions using Python's datetime module to handle dates, times, and durations. These basic functions are essential for your rocket delivery service. In this project, you will make simple reusable functions for working with timestamps, calculating rocket landing times based on launch and travel duration, and figuring out days until a delivery deadline to keep those customers updated!

This project is data-less, but you can test your functions by calling them in the workspace and passing them the required variables.

#1 Define a function called format_date(), which formats a timestamp into a readable datetime string.

It must accept two parameters: timestamp - the Unix timestamp integer, and datetime_format - a string specifying the desired date format.
The function should return the date correctly formatted as a string.
For example, calling format_date(1514665153, "%d-%m-%Y") should output "30-12-2017".

```python
from datetime import datetime, timedelta

def format_date(timestamp: float, datetime_format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Formats a timestamp into a readable datetime string.

    Args:
        timestamp (float): Unix timestamp value e.g. 1727172895.0
        datetime_format (str): Output format string. Defaults to "%Y-%m-%d %H:%M:%S"

    Returns:
        str: Formatted datetime string e.g. "2026-09-24 11:34:55"
    """
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime(datetime_format)

print(format_date(1727172895.0))
# print(format_date(1727172895.0, "%B %d, %Y"))
```

#2 Define a function called calculate_landing_time(), which calculates the estimated landing time.

It must accept two parameters: rocket_launch_dt - the rocket launch datetime object, and travel_duration - the expected travel time in days as an integer.
The function should return the estimated Mars landing time as a datetime string in the format DD-MM-YYYY.
For example, calling calculate_landing_time(datetime(2023, 2, 15), 20) should output "07-03-2023".

```python
from datetime import datetime, timedelta

def calculate_landing_time(rocket_launch_dt: datetime, travel_duration: int) -> str:
    """
    Calculates the estimated Mars landing time.

    Args:
        rocket_launch_dt (datetime): The rocket launch datetime object.
        travel_duration (int): Expected travel time in days.

    Returns:
        str: Estimated Mars landing time in DD-MM-YYYY format.
    """
    landing_dt = rocket_launch_dt + timedelta(days=travel_duration)
    return landing_dt.strftime("%d-%m-%Y")

# Usage
launch = datetime(2026, 9, 24, 11, 34, 55)
print(calculate_landing_time(launch, 259))  # '10-06-2027'
```

#3 Define a function named days_until_delivery(), which calculates the days until a package arrives for customers.

It must accept two parameters: expected_delivery_dt - the estimated delivery date as a datetime object for the package, and current_dt - the current date as a datetime object.
The function should calculate the difference in days between the expected delivery datetime and the current datetime, then return the number of days remaining as an integer.
For example, calling days_until_delivery(datetime(2023, 2, 15), datetime(2023, 2, 5)) should output 10.

```python
from datetime import datetime, timedelta

def days_until_delivery(expected_delivery_dt: datetime, current_dt: datetime) -> int:
    """
    Calculates the number of remaining days until package delivery.
    
    Parameters:
    expected_delivery_dt (datetime): The estimated delivery date and time.
    current_dt (datetime): The current date and time.
    
    Returns:
    int: The number of days remaining until delivery.
    """
    # Subtracting two datetime objects returns a timedelta object
    time_difference = expected_delivery_dt - current_dt
    
    # Extract and return the integer days attribute from the timedelta object
    return time_difference.days

# Example dates
current = datetime(2026, 10, 1, 10, 0)
expected = datetime(2026, 10, 5, 14, 30)

# Calculate remaining days
remaining_days = days_until_delivery(expected, current)
print(f"Days until delivery: {remaining_days}")  # Output: Days until delivery: 4
```
