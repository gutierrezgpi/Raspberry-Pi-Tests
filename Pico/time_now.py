# Core Modules
from time import localtime

# Routine
time_now = localtime()

print(f"Controller output: {time_now}")

year, month, day, hour, minute, second, weekday, yearday, daylight = time_now

time_now = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, day, hour, minute, second)

print(f"Formatted output: {time_now}")

'''
Output:

Controller output: struct_time(tm_year=2024, tm_mon=9, tm_mday=27, tm_hour=21, tm_min=21, tm_sec=34, tm_wday=4, tm_yday=271, tm_isdst=-1)
Formatted output: 2024-09-27 21:21:34

'''