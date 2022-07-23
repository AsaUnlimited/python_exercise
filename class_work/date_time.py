from datetime import datetime, timedelta

d1 = datetime.now()
d2 = datetime(2020, 5, 27)
diff = d1 - d2
print(type(diff))

t = timedelta(weeks=1)
print(d1 + t)

date_from_str = datetime.strptime("2022-02-02 10:5:55", "%Y-%m-%d %H:%M:%S")
# date_from_str2 = datetime.strftime(2022 - 02 - 02, "%Y-%m-%d")

print(d1.strftime("%A"))
print(d1.strftime("%B"))
print(d1.strftime("%A%d, %B %y"))


print(date_from_str)