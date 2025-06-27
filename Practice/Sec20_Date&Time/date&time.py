import datetime
import pytz

                        # Date and time

# Importing datetime m
# 1. Current Date and Time
now = datetime.datetime.now()
print("Current Date and Time:"),


# 2. Current Date
current_date = datetime.date.today()
print("Current Date:", current_date)


# 3. Creating a Specific Date
specific_date = datetime.date(2023, 12, 25)
print("Specific Date:", specific_date)


# 4. Creating a Specific Time
specific_time = datetime.time(14, 30, 15)
print("Specific Time:", specific_date)


# 5. Formatting Dates and Times
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted)


# 6. Parsing Dates from Strings
date_str = "2024-06-01"
parsed_date = datetime.datetime.strptime(date_str,"%Y-%m-%d")
print("Parsed Date:", parsed_date)


# 7. Date Arithmetic (timedelta)
delta = datetime.timedelta(days=7)
future_date = current_date + delta
print("Date after 7 days:", future_date)


# 8. Difference Between Dates
date1 = datetime.date(2024, 6, 1)
date2 = datetime.date(2024, 5, 20)
difference = date1 - date2
print("Difference between dates:", difference.days)


# 9. Getting Weekday
weekday = current_date.weekday()  # Monday is 0
print("Weekday (0=Monday):", weekday)


# 10. ISO Calendar
iso_calendar = current_date.isocalendar()
print("ISO Calendar (Year, Week number, Weekdaiso_cale")


# 11. Getting UTC Time
utc_now = datetime.datetime.utcnow()
print("Current UTC Time:", utc_now)


# 12. Timezone-aware Datetime
utc = pytz.UTC
aware_now = datetime.datetime.now(utc)
print("Timezone-aware Current Time:", aware_now)


# 13. Adding Hours/Minutes/Seconds
add_hours = now + datetime.timedelta(hours=5)
print("Time after 5 hours:", add_hours)


# 14. Getting Month, Day, Year, etc.
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)