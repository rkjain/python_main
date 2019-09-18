import time
import concurrent.futures


# Do tasks synchronusly
start = time.perf_counter()

def sleep_fewsec(n):
	print(f'Sleeping for {n} seconds')
	time.sleep(n)
	return 'Sleep Completed'



with concurrent.futures.ThreadPoolExecutor() as executor:
	f1 = executor.submit(sleep_fewsec, 10)
	f2 = executor.submit(sleep_fewsec, 10)
	
	print(f1.result())
	print(f2.result())

finish = time.perf_counter()
print(round(finish - start,2))

