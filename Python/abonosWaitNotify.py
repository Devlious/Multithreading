import threading
import time
import random

abono = True 

class BankAccount(threading.Thread):
    acctBalance = 10

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
        global abono

        money_request = random.randrange(100)+1

        condition.acquire()

        while BankAccount.acctBalance - money_request < 0 and abono == False:
            print("{} waiting for money [${}]".format(self.name, money_request))
            condition.wait()

        print("- {} tries to withdrawal ${}".format(self.name, money_request))

        condition.release()

        BankAccount.acctBalance -= money_request
        if BankAccount.acctBalance < 0:
            abono = False
        print("New account balance is : ${}".format(BankAccount.acctBalance))

        print("\n")
        time.sleep(0.5)

    def set_money(self):
        global abono
        money_request = random.randrange(100)+1
        condition.acquire()
        print("+ {} deposit : ${}".format(self.name, money_request))

        BankAccount.acctBalance += money_request
        print("New account balance is : ${}".format(BankAccount.acctBalance))
        if not abono and BankAccount.acctBalance >= 0:
            abono = True

        condition.notifyAll()
        condition.release()

        print("\n")
        time.sleep(0.5)



# Create a lock to be used by threads
threadLock = threading.Lock()
condition = threading.Condition()

threads = [BankAccount("Beto"), BankAccount("Diego"), BankAccount("Lolo")]

for t in threads:
    t.start()