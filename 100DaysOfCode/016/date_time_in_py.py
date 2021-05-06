import datetime
print(dir(datetime))

from datetime import datetime
now = datetime.now()
print(now)                      # 2019-12-04 23:34:46.549883
day = now.day                   # 4
month = now.month               # 12
year = now.year                 # 2019
hour = now.hour                 # 23
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 4/12/2019, 23:38
