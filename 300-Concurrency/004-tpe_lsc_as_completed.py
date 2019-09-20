import concurrent.futures
import time

def test_function(duration, name):
	print('Start: ',name)
	time.sleep(duration)
	print('End: ',name)
	return 'Process %s Slept for Duration %s Seconds' % (name, duration)


# results consists of future object
# as completed returns furture objects as they are completed

with concurrent.futures.ThreadPoolExecutor() as executor:
	durations = [5,8,10]
	results = [ executor.submit(test_function, duration, 'f-{name}'.format(name=duration)) for duration in durations ]

	for f in concurrent.futures.as_completed(results):
		print(f.result())


