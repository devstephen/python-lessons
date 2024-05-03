from datetime import datetime


print(datetime(1999, 7, 24, 23, 12, 12))
print(datetime(1999, 7, 24, 23))

print(datetime(year=1999, month=7, day=24, hour=14, minute=16, second=23))


today = datetime.today()
now = datetime.now()
print()
print(today)
print(now)

print(today.weekday())

same_time = today.replace(year=1999)
print(same_time)

same_time_jan = today.replace(month=1)
print(same_time_jan)