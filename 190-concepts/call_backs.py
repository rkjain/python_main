#!/usr/bin/env python3
import time

"""
	Callback is a fucntion that is passed to the main function
	as an argument. Callbacks are executed when the main function
	finishes execution.
"""

def main_function(mf_arg, cb_function, cb_arg):
	print('Execute Task: ', mf_arg)
	time.sleep(10)
	print('Finishing Task: ', mf_arg)
	cb_function(cb_arg)


def cb_function(something):
	time.sleep(2)
	print('Starting  Cleanup: ',something)
	print('Finished Cleanup: ',something)


main_function('Deployment', cb_function, 'Temp Data')