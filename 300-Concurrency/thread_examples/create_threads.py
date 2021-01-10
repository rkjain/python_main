#!/usr/bin/env python3

from threading import Thread, current_thread, main_thread
from time import sleep
import subprocess
import shlex

# how to create a thread

class MyThread:
	def display(self, name):
		for i in range(1,11):
			print("Thread Name: %s or %s , Count: %s" % (current_thread().getName(), name, i))
			#subprocess.run(shlex.split("ping -c 1 www.google.com"))
			sleep(1)

if __name__ == "__main__":

	# get thread name
    # condition that you can use with main thread

	if current_thread() == main_thread():
	    print("Main Thread Name: ", current_thread().getName())

	## daemon threads and join

	#t1 = Thread(target=MyThread().display, daemon=True)
	#t2 = Thread(target=MyThread().display, daemon=True)
	#t3 = Thread(target=MyThread().display, daemon=True)
	#t4 = Thread(target=MyThread().display, daemon=True)
	#t1.join()
	#t2.join()
	#t3.join()
	#t4.join()

	t1 = Thread(target=MyThread().display, args=('alpha-1',))
	t2 = Thread(target=MyThread().display, args=('alpha-2',))
	t3 = Thread(target=MyThread().display, args=('alpha-3',))
	t4 = Thread(target=MyThread().display, args=('alpha-4',))

	t1.start()
	t2.start()
	t3.start()
	t4.start()
