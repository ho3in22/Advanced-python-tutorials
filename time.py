from datetime import datetime, date
now = datetime.now()

print(now.strftime("%Y/%m/%d"))

timestamp = datetime.timestamp(now)
print(timestamp)

dt_obj = datetime.fromtimestamp(timestamp)
print(dt_obj)

from datetime import timedelta
delta_time = timedelta(weeks=1)

next_week = now + delta_time
print(next_week)

date1 = date(2025,12,2)
date2 = date(2025,12,22)
print(date2 - date1)

datetime1 = datetime(2025,12,2,13,43,22)
datetime2 = datetime(2025,12,22,8,23,12)
print(datetime2 - datetime1)