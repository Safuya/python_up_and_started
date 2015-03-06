from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


print(timedelta(days=365, hours=5, minutes=1))

print("Today is:", str(datetime.now()))
print("15 days, 14 hours ago it was:", str(datetime.now() - timedelta(days=15, hours=14)))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was", s)

today = date.today()
april_fools_day = date(today.year, 4, 1)
if april_fools_day < today:
    print("April Fool's day already went by %d days ago" % ((today-april_fools_day).days))
    april_fools_day = april_fools_day.replace(year = today.year + 1)

time_to_april_fools_day = abs(april_fools_day - today)
print(time_to_april_fools_day.days, "days until next April Fools Day")
