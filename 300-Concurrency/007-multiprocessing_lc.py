#!/usr/bin/env python3

import concurrent.futures
import time


def sleep_function(duration, name):
	print('Start Sleep: ', name)
	time.sleep(2)
	print('End Sleep: ', name)
	return str(name) + " completed"


with concurrent.futures.ProcessPoolExecutor() as executor:
	results = [ executor.submit(sleep_function, 2, name) for name in range(1,11)]

for f in concurrent.futures.as_completed(results):
	print(f.result())


print('Hello World!')

