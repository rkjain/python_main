#!/usr/bin/env python3

import concurrent.futures
import time


def sleep_function(duration, name):
	print('Start Sleep: ', name)
	time.sleep(2)
	print('End Sleep: ', name)
	return str(name) + " completed"


with concurrent.futures.ProcessPoolExecutor() as executor:
	name = ['a','b','c']
	duration = [20, 19, 12]
	results = executor.map(sleep_function, duration, name)

for result in results:
	print(result)
