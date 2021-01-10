#!/usr/bin/env python3
from threading import *
from time import *

# Thread communication using boolean flag

class Producer:

	def __init__(self):
		self.orders = []
		self.status = False

	def produce(self, n):
		tn = current_thread().getName()
		for i in range(1, n + 1):
			print("%s => Preparing Order: Item - %s" % (tn, i))
			self.orders.append("Item - %s" % (i))
			sleep(1)
		print("%s => Orders Ready to Ship" % (tn))
		self.status = True

class Consumer:
	def __init__(self, prod):
		self.prod = prod

	def consume(self):
		tn = current_thread().getName()
		while not self.prod.status:
			print("%s => Checking Order Status: " %(tn), "No items available for shipping")
			sleep(.2)
		print("Shipping Items: ")
		for i in self.prod.orders:
			print(i)

prod = Producer()
con = Consumer(prod)

t1 = Thread(target=prod.produce, args=(15,))
t2 = Thread(target=con.consume)

t1.start()
t2.start()
