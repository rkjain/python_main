import concurrent.futures
import time

# map returns result

def test_function(duration, name):
	print('Start: ',name)
	time.sleep(duration)
	print('End: ',name)
	return 'Process %s Slept for Duration %s Seconds' % (name, duration)


with concurrent.futures.ThreadPoolExecutor() as executor:
	durations = [5,8,10]
	names = ['p1','p2' ,'p3']
	results = executor.map(test_function, durations, names )
	for result in results:
		print(result)



