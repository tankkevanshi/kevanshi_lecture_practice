
# 1.Date Time Module in python

# The datatime module in used the to work with dates and times in python.

# Get Current date and time module.
# Create custom dates.
# Formate dates.
# Perform date clculations.

# Importing datatime module

import datetime

now = datetime

print(now)

# current date only

today = datetime.date.today()

print(today)

# Custom date

custom = datetime.date(2024,12,24)

print(custom)

#  Acess Year,Month,Day

today = datetime.date.today()

print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# Strftime() is used formate date and time.

now = datetime.datetime.now()

formated = now.strftime("%d-%m-%Y:%H:%M:%S")

print(formated)

# date differnce

d1 = datetime.date(2009,2,3)
d2 = datetime.date(2026,6,11)

differnce = d2-d1

print(differnce.days)

# 2. time module in python

# working with system time.
# Deaitls in proframe
# mesuring execution time

# import time module

import time

current = time.time()
print(current)

# It returns secounds from january 1,1970

# pause program using sleep()

print("starts")

time.sleep(3)
print("End after 3 secound")

# current local time

local = time.localtime()

print(local)

# formate time

current = time.strftime("%H:%M:%S")

print(current)

# Measure exection time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Exceution Time:",end-start)

#1. Display current date and time
from datetime import datetime

now = datetime.now()
print(now)
print("year:",now.year)
print("month:",now.month)
print("day:",now.day)
print("minute:",now.minute)
print("second:",now.second)

#1. datetime.datetime.now()
# returns current date and time

#2. datetime.date.today()
# returns current date.

#3. datetime.datetime.today()
# returns current local date and time.

#4. datetime.datetime.utcnow()
# returns current UTC time.

import datetime

print(datetime.datetime.utcnow)

#5. strftime()
# converts string int datatime into string.

#6.srftime()
# converts string into datatime object.

from datetime import datetime

date = "2025-06-11"

obj = datetime.strptime(date, "%Y-%m-%d") 

print(obj)

#7. timedata
# used to date calculation

from datetime import datetime,timedelta

today = datetime.now()

future = today + timedelta(days = 5)

print(future)

#8. replace()
# Replaces year month / day etc...

now = datetime.now()

new=date = now.replace(year = 2030)

print(new-date)

#9. date()

# Extract onlu date

#10. time

# Extract only time.

#11. Week days()

# return weekday number

now=datetime.now()

print(now.weekday())

#12. isoweekday()

# return readble weekdays number(1-7)

now=datetime.now()

print(now.isoweekday())

#13.ctime

# return readable date and time

now=datetime.now()

print(now,time)

#14. timestamp()

# return secound since epoch.

now = datetime.now()

print(now.timestamp())

#15. fromtimestamp()

# converts timestamp to datetime.

s = 1749863000

print(datetime.fromtimestamp(s))


# python time module method

#1. time()
#2. ctime()
#3. sleep()
#4. localtime()
#5. gmtime()

# returns UTC time object.

import time

print(time.gmtime())

#6. strftime()
#7. strptime()
#8. mktime()

# converts time tuple in secounds

import time

t = time.localtime()

print(time.mktime(t))

#9. asctime()

import time

t = time.localtime()

print (time.mktime(t))

#9. asctime()

import time

t = time.localtime()

print(time. asctime(t))

#10. perf_counter()

#11. process_time()

#12. monotonic()

# returns contunuesly in creasung clock value.

import time

print(time.monotonic)





