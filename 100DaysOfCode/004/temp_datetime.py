import datetime

dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")

print(dt)

print(datetime.datetime.today())
print(datetime.datetime.now())


day_delta = datetime.timedelta(days=1)
start_date = datetime.date.today()
end_date = start_date + 7*day_delta

for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)
