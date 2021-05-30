import datetime
#from datetime import datetime

time = datetime.time(2,20,1,10)

print(time)

print(time.minute)
print(time.microsecond)

today = datetime.date.today()

print(today.ctime())


dateandtime = datetime.datetime(2021,10,3,2,29,20)

print(dateandtime.date())

dateandtime = dateandtime.replace(year=2020)

print(dateandtime.date())

date1 = datetime.date(2021,10,3)
date2 = datetime.date(2020,10,3)

print((date1-date2).days)

datetime1 = datetime.datetime(2021,10,3,2,20,1)
datetime2 = datetime.datetime(2020,10,3,2,10,1)

print(datetime1-datetime2)