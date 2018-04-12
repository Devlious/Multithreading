import threading
import time
import random

class self(threading.Thread):
    acctBalance = 50
    abono = True

    def __init__(self, name, acctBalance):
        threading.Thread.__init__(self)
        self.name = name
        self.acctBalance = acctBalance

    def run(self):
        # Call the static method
        for _ in range(25):
            # print(":: {} ::".format(time.strftime("%H:%M:%S", time.gmtime())))
            if random.randrange(2)+1 == 1:
                self.set_money()
            else:
                self.get_money()

    def get_money(self):

        money_request = random.randrange(100)+1

        condition.acquire()

        while self.acctBalance - money_request < 0 and self.abono == False:
            print("~~ {} waiting for money [${}]".format(self.name, money_request))
            condition.wait()

        print("- {} tries to withdrawal ${}".format(self.name, money_request))

        condition.release()

        self.acctBalance -= money_request
        if self.acctBalance < 0:
            self.abono = False

        if self.acctBalance >= 0:
            print("{}'s account balance is : ${}".format(self.name, self.acctBalance))
        else:
            print("{}'s account balance is : ${} with debt ${}".format(self.name, 0, -self.acctBalance))

        print("\n")
        time.sleep(0.5)

    def set_money(self):
        money_request = random.randrange(100)+1
        condition.acquire()
        print("+ {} deposit : ${}".format(self.name, money_request))

        self.acctBalance += money_request
        if self.acctBalance >= 0:
            print("{}'s account balance is : ${}".format(self.name, self.acctBalance))
        else:
            print("{}'s account balance is : ${} with debt ${}".format(self.name, 0, -self.acctBalance))
        if not self.abono and self.acctBalance >= 0:
            self.abono = True

        condition.notifyAll()
        condition.release()

        print("\n")
        time.sleep(0.5)



# Create a lock to be used by threads
threadLock = threading.Lock()
condition = threading.Condition()

threads = [self("Beto", 100), self("Diego", 200), self("Lolo", 300)]

for t in threads:
    t.start()