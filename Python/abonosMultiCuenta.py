import threading
import random
import time

class Account():

	def __init__(self, name, acctBalance):
		self.name = name
		self.acctBalance = acctBalance
		self.abono = True

	def get_money(self, name):
		money_request = random.randrange(100)+1

		condition.acquire()

		while self.acctBalance - money_request < 0 and self.abono == False:
			print("~~ {} waiting for money [${}]".format(name, money_request) )
			condition.wait()

		print("- {} tries to withdrawal ${} from {}'s account".format(name, money_request, self.name) )

		condition.release()

		self.acctBalance -= money_request
		if self.acctBalance < 0:
			self.abono = False

		if self.acctBalance >= 0:
			print("{}'s account balance is : ${}".format(self.name, self.acctBalance) )
		else:
			print("{}'s account balance is : ${} with debt ${}".format(self.name, 0, -self.acctBalance) )

		print("\n")
		time.sleep(0.5)

	def set_money(self, name):
		money_request = random.randrange(100)+1
		condition.acquire()
		print("+ {} deposit : ${} to {}'s account".format(name, money_request, self.name))

		self.acctBalance += money_request
		if self.acctBalance >= 0:
			print("{}'s account balance is : ${}".format(self.name, self.acctBalance))
		else:
			print("{}'s account balance is : ${} with debt ${}".format(self.name, 0, self.acctBalance))

		if not self.abono and self.acctBalance >= 0:
			self.abono = True

		condition.notifyAll()
		condition.release()

		print("\n")
		time.sleep(0.5)

class Person(threading.Thread):

	def __init__(self, name, accounts):
		threading.Thread.__init__(self)
		self.name = name
		self.accounts = accounts

	def run(self):
		for _ in range(5):
			Person.setAction(self)

	def setAction(self):
		user = random.randrange(4)+1

		if random.randrange(2)+1 == 1:
			accounts[user].get_money(self.name)
		else:
			accounts[user].set_money(self.name)

condition = threading.Condition()

persons = ["Beto", "Alan", "Fer", "Mario", "Lolo"]

accounts = [ Account(x, random.randrange(500)+1) for x in persons]

for p in persons:
	Person(p, list(filter(lambda a: a.name != p, accounts)) ).start()
