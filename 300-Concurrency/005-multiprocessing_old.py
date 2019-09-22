#!/usr/bin/env python3

import multiprocessing
import time


def sleep_function(duration, name):
	print('Start Sleep: ', name)
	time.sleep(2)
	print('End Sleep: ', name)
	return name + " completed"


f1 = multiprocessing.Process(target=sleep_function, args=[2, 'f1'])
f2 = multiprocessing.Process(target=sleep_function,args=[2, 'f2'])

f1.start()
f2.start()

f1.join()
f2.join()
