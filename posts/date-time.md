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
