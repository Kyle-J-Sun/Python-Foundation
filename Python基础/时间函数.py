import time
import calendar
#return current timestamp
t = time.time()
print(t)
#timestamp can be transferred to time tuple in current time zone
tup1 = time.localtime(t)
print(tup1)
print(tup1.tm_wday)
#transfer time tuple to timestamp
print(time.mktime(tup1))
#acquire CPU time, machine time
print(time.clock())
time.sleep(5)
print(time.clock())
time.sleep(10)
print(time.clock())
#formatting time tuple
t = time.time()
print(t)
tup1 = time.localtime(t)
time_format = time.strftime('%Y-%m-%d %H:%M:%S',tup1)
print(time_format)
time_for = time.strptime(time_format,'%Y-%m-%d %H:%M:%S')
print(time_for)
import calendar
t = calendar.calendar(2018,w=2,l=1,c=6)
print(t)