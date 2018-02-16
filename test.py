import datetime
import math

now = datetime.datetime.now()
past = datetime.datetime(now.year, now.month - (0-1), 1) - (datetime.timedelta(days=1))
LOM = datetime.datetime(past.year, past.month, past.day, hour=23, minute=59, second=59)

days_remaining = LOM.day - now.day

print(days_remaining)
print(now.day)
print(LOM.day)

runs_per_week = 3
avg1 = runs_per_week/7
runs_remain = math.ceil(days_remaining*avg1)

print("how many runs remain?")
print(math.ceil(days_remaining*avg1))

print("DAY OF YEAR")
timestamp = datetime.datetime.now()
day_of_year = datetime.datetime.now().timetuple().tm_yday
#days_in_the_year = (timestamp - datetime.datetime.date(timestamp.year,1,1)).days + 1
print(day_of_year)
