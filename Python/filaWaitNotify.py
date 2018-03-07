import threading
import random
import time

class ArrayManagement(threading.Thread):
    arr = []

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        for _ in range(5):
            if random.randrange(2)+1 == 1:
                ArrayManagement.add_num(self)
            else:
                ArrayManagement.remove_num(self)

    def remove_num(self):
        condition.acquire()

        while len(self.arr) <= 0:
            print("{} waiting for nums".format(self.name))
            condition.wait()

        print("{} was popped from array".format(self.arr[0]))
        self.arr.pop(0)
        print("{} final array".format(self.arr))

        condition.notifyAll()
        condition.release()

        print("\n")
        time.sleep(0.5)

    def add_num(self):
        num = random.randrange(10)

        condition.acquire()

        while len(self.arr)+1 > 5:
            print("{} waiting for space".format(self.name))
            condition.wait()

        self.arr.append(num)
        print("{} was added to array".format(num))
        print("{} final Array".format(self.arr))

        condition.notifyAll()
        condition.release()

        print("\n")
        time.sleep(0.5)


# Create a lock to be used by Threads
threadLock = threading.Lock()
condition = threading.Condition()

threads = [ArrayManagement("Beto"), ArrayManagement("Diego"), ArrayManagement("Lolo")]

for t in threads:
    t.start()