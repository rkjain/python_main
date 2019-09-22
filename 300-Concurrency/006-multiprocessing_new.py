#!/usr/bin/env python3

import concurrent.futures
import time


def sleep_function(duration, name):
	print('Start Sleep: ', name)
	time.sleep(2)
	print('End Sleep: ', name)
	return name + " completed"


with concurrent.futures.ProcessPoolExecutor() as executor:
	f1 = executor.submit(sleep_function, 2, 'f1')
	f2 = executor.submit(sleep_function, 2, 'f2')

f1.result()
f2.result()

print('Hello World!')

