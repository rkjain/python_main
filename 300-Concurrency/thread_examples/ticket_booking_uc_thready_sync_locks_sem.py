#!/usr/bin/env python3

from threading import *
from time import sleep

class BookTicket:

	"""
		Thread Synchronization using
			- Locks
			- Semaphores
	"""

	def __init__(self, total_seats):
		self.total_seats = total_seats
		self.lock = Lock()
		#self.lock = Semaphore()
		
	def buy(self,seats_requested):
		self.lock.acquire()
		thread_name = current_thread().getName()
		print("%s: Total Seats Available: " % (thread_name), self.total_seats)
		if seats_requested <= self.total_seats:
			print("%s: Checking Seat Availalbity" % (thread_name))
			sleep(1)
			print("%s: Confirming And Booking Seats: " % (thread_name), seats_requested)
			sleep(1)
			print("%s: Processing Payment" % (thread_name))
			sleep(1)
			print("%s: Printing Ticket" % (thread_name))
			sleep(1)
			print("%s: Emailing Ticket" % (thread_name))
			self.total_seats -= seats_requested
		else:
			print("Thread %s: Sorry! No more tickets left" % (thread_name))
		self.lock.release()

obj = BookTicket(20)

t1 = Thread(target=obj.buy, args = (13,))
t2 = Thread(target=obj.buy, args = (4,))
t3 = Thread(target=obj.buy, args = (5,))

t1.start()
t2.start()
t3.start()
