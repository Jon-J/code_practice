import threading
import time

class CustomThread(threading.Thread):
    def __init__(self, threadID, name, count):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.count = count

    def run(self):
        print("Starting "+self.name)
        print_time(self.name, self.count, 5)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s:%s"% (threadName, time.ctime(time.time())))
        counter -=1

thread1 = CustomThread(1, "thread1", 3)
thread2 = CustomThread(2, "thread2", 2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting main process....")
