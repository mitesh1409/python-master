SQL_SESSIONS = """
    select distinct date(created_at) as session_date
    from times
"""

SQL_SWIMMERS_BY_SESSION = """
    select distinct swimmers.name, swimmers.age
    from swimmers
    join times on times.swimmer_id = swimmers.id
    where date(times.created_at) = :date
    order by swimmers.name
"""

SQL_SWIMMERS_EVENTS_BY_SESSION = """
    select distinct events.distance, events.stroke
    from times
    join swimmers on times.swimmer_id = swimmers.id
    join events on times.event_id = events.id
    where (swimmers.name = :name and swimmers.age = :age) and
    date(times.created_at) = :date
"""

SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION = """
    select times.time
    from times
    join swimmers on times.swimmer_id = swimmers.id
    join events on times.event_id = events.id
    where (swimmers.name = :name and swimmers.age = :age) and
    (events.distance = :distance and events.stroke = :stroke) and
    date(times.created_at) = :date
"""
