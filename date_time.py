
# %%

from datetime import date, datetime, timedelta, time, timezone


date_1 = date(2000, 10, 11)
date_2 = date(year=2000, month=10, day=11)
date_3 = date.today()
date_diff = date_3-date_1
date_1_str_1 = date_1.strftime('%Y/%m/%d')
date_1_str_2 = date_1.strftime('%b %d, %d')

time_1 =  time(hour=2)
time_2 =  time(hour=2, minute=30)
time_3 =  time(hour=2, minute=30, second=30)
time_4 =  time(hour=2, minute=30, second=30, microsecond=50)

datetime_1 = datetime(2012,11,12,13,14,15,16)
datetime_2 = datetime(
    year=2000,
    month=10,
    day=11,
    hour=12,
    minute=13,
    second=14,
    microsecond=15
    )
datetime_3 = datetime.now()
datetime_diff_1_2 = datetime_1 - datetime_2

d1 = timedelta(hours=11)
d2 = timedelta(days=3, hours=62, minutes=33, seconds=44)

tz1 = timezone(offset=timedelta(hours=5, minutes=45))

print(f'date_1 = {date_1}')
print(f'date_2 = {date_2}')
print(f'date_3 = {date_3}')
print(f'date_diff = {date_diff}')
print(f'date_1_str_1 = {date_1_str_1}')
print(f'date_1_str_2 = {date_1_str_2}')

print(f'time_1 = {time_1}')
print(f'time_2 = {time_2}')
print(f'time_3 = {time_3}')
print(f'time_4 = {time_4}')

print(f'datetime_1 = {datetime_1}')
print(f'datetime_2 = {datetime_2}')
print(f'datetime_3 = {datetime_3}')
print(f'datetime_diff_1_2 = {datetime_diff_1_2}')

print(f'd1 = {d1}')
print(f'd1 = {d2}')

print(f'tz1 = {tz1}')

# %%

import datetime

y = datetime.datetime.now()
print(y)
print(y.year)
print(y.strftime("%A"))         # Weekday(Sunday)
print(y.strftime("%X"))         # Local Time
print(y.strftime("%d"))         # Day of month 0-31
print(y.strftime("%m"))         # Month as a number 01-12
print(y.strftime("%Y"))         # Year
print(y.strftime("%H"))         # Hour 0-24
print(y.strftime("%p"))         # AM/PM
print(y.strftime("%M"))         # Minute
print(y.strftime("%S"))         # Second
print(y.strftime("%f"))         # Microsecond
print(y.strftime("%z"))         # UTC offset
print(y.strftime("%Z"))         # Timezone
print(y.strftime("%c"))         # Local version of date and time
print(y.strftime("%x"))         # Local version of date
print(y.strftime("%X"))         # Local version of time

x = datetime.datetime(2020, 5, 17)
print(x)

z = datetime.date.today()
print(z)
