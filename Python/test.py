import threading
import time
import random

class BankAccount(threading.Thread):
    acctBalance = 500
    moneyRequest = 0

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # Get lock to keep other threads from accessing the account
        threadLock.acquire()

        # Call the static method
        for _ in range(5):
            self.moneyRequest = random.randrange(100)+1
            print(":: {} ::".format(time.strftime("%H:%M:%S", time.gmtime())))
            if random.randrange(2)+1 == 1:
                BankAccount.setMoney(self)
            else:
                BankAccount.getMoney(self)
            print("\n")
            time.sleep(0.5)

        # Release lock so other thread can access the account
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${}".format(customer.name,
                                                  customer.moneyRequest))

        if BankAccount.acctBalance - customer.moneyRequest > 0:
            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance is : ${}".format(BankAccount.acctBalance))
        else:
            print("Not enough money in the account")
            print("Current balance : ${}".format(BankAccount.acctBalance))

    @staticmethod
    def setMoney(customer):
        print("{} tries to deposit : ${}".format(customer.name,
                                                     customer.moneyRequest))
        BankAccount.acctBalance += customer.moneyRequest
        print("New account balance is : ${}".format(BankAccount.acctBalance))



# Create a lock to be used by threads
threadLock = threading.Lock()

threads = [BankAccount("Beto"), BankAccount("Diego"), BankAccount("Lolo")]

for t in threads:
	t.start()
	t.join()


print("Execution Ends")
