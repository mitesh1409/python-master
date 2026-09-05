SQL_SESSIONS = """
    select distinct created_at
    from times
"""

SQL_SWIMMERS_BY_SESSION = """
    select distinct swimmers.name, swimmers.age
    from swimmers, times
    where times.swimmer_id = swimmers.id and
    date(times.created_at) = ?
    order by swimmers.name
"""

SQL_SWIMMERS_EVENTS_BY_SESSION = """
    select distinct events.distance, events.stroke
    from swimmers, events, times
    where times.swimmer_id = swimmers.id and
    times.event_id = events.id and
    (swimmers.name = ? and swimmers.age = ?) and
    date(times.created_at) = ?
"""

SQL_CHART_DATA_BY_SWIMMER_EVENT_SESSION = """
    select times.time
    from swimmers, events, times
    where times.swimmer_id = swimmers.id and
    times.event_id = events.id and
    (swimmers.name = ? and swimmers.age = ?) and
    (events.distance = ? and events.stroke = ?) and
    date(times.created_at) = ?
"""
