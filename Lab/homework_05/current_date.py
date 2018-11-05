import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")
# now = datetime.datetime.now()
# print(now.hour, now.minute, sep =":", end = " - ")
# print(now.day, now.month, now.year, sep = "/")
print(now)