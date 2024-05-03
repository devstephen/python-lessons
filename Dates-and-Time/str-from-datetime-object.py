from datetime import datetime

today = datetime.today()
print(today)
print(today.strftime("%m"))
print(today.strftime("%m/%d/%Y"))
print(today.strftime("%m-%d-%Y"))


print()
print(today.strftime("%y-%m-%d"))

print()
print(today.strftime("%A %B %y"))