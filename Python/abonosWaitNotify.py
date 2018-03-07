import threading
import time
import random

class BankAccount(threading.Thread):
    acctBalance = 50

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # Call the static method
        for _ in range(5):
            # print(":: {} ::".format(time.strftime("%H:%M:%S", time.gmtime())))
            if random.randrange(2)+1 == 1:
                BankAccount.set_money(self)
            else:
                BankAccount.get_money(self)

    def get_money(self):
        money_request = random.randrange(100)+1

        condition.acquire()
        while BankAccount.acctBalance - money_request < 0:
            print("{} waiting for money [${}]".format(self.name, money_request))
            condition.wait()

        print("- {} tries to withdrawal ${}".format(self.name, money_request))

        condition.release()

        BankAccount.acctBalance -= money_request
        print("New account balance is : ${}".format(BankAccount.acctBalance))

        print("\n")
        time.sleep(0.5)

    def set_money(self):
        money_request = random.randrange(100)+1
        condition.acquire()
        print("+ {} deposit : ${}".format(self.name, money_request))

        BankAccount.acctBalance += money_request
        print("New account balance is : ${}".format(BankAccount.acctBalance))
        condition.notifyAll()
        condition.release()

        print("\n")
        time.sleep(0.5)



# Create a lock to be used by threads
threadLock = threading.Lock()
condition = threading.Condition()

threads = [BankAccount({"Beto":0}), BankAccount({"Diego":0}),
           BankAccount({"Lolo":0})]

for t in threads:
    t.start()
