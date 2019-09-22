import time
from threading import Thread

# Do tasks synchronusly
start = time.perf_counter()

def sleep_fewsec(n):
	print(f'Sleeping for {n} seconds')
	time.sleep(n)
	print('Sleep Completed')


all_threads = []

for _ in range(10):
	t = Thread(target=sleep_fewsec, args=(10,))
	all_threads.append(t)
	t.start()

print(all_threads)
for thread in all_threads:
	thread.join()
	print('Thread Completed: ', thread.name)


# t2 = Thread(target=sleep_fewsec, args=(5,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()


finish = time.perf_counter()
print(round(finish - start,2))
