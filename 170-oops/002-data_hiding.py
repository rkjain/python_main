'''
Data Hiding
  - Abstraction
  - Encapsulation

Encapsulation in OOP refers to binding the data and the methods to 
manipulate that data together in a single unit, that is, class.
'''
class Login(object):

	def __init__(self, username, password):
		self.__username = username
		self.__password = password

	def login(self, username, password):
		if self.__username == username and self.__password == password:
			print('Login Successfull!')
		else:
			print('Try Again!')

accountOne = Login('rishabh', 'P@ssw0rd1234')
accountOne.login('rishabh', 'P@ssw0rd1234')
accountOne.login('rishabh', 'Wrong Password')

