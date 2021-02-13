#!/usr/bin/env python3

import time
import datetime

# Number of seconds since Jan 1, 1970
epoch = time.time()

# Current Time
current_time = time.ctime(epoch)
print(current_time)

# Date Time
current_time = datetime.datetime.today()
print('Year: ', current_time.year)
print('Month: ', current_time.month)
print('Day: ', current_time.day)
print('Min: ', current_time.minute)
print('Hour: ', current_time.hour)
print('Seconds: ', current_time.second)

