from datetime import date, time, datetime, timedelta, timezone

# date(year, month, day)
today = date(2026, 5, 9)
print("Date:", today)

# time(hour, minute, second, microsecond)
current_time = time(14, 30, 45)
print("Time:", current_time)

# datetime(year, month, day, hour, minute, second)
current_datetime = datetime(2026, 5, 13, 14, 30)
print("Datetime:", current_datetime)

# timedelta(days, hours, minutes, weeks, etc.)
future_date = today + timedelta(days=7)
print("Future Date:", future_date)

# timezone(timedelta(hours=offset))
est = timezone(timedelta(hours =- 5))

# datetime.now(timezone)
utc_time = datetime.now(timezone.utc)
print("UTC Time:", utc_time)