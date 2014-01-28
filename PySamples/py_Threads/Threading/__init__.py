
import threading
import time
import random

class Task(threading.Thread):
    
    lock = threading.Lock()
    Counter = 0
    
    def __init__(self, duration, loop):
        threading.Thread.__init__(self)
        self.duration = duration
        self.loop = loop
        Task.Counter = Task.Counter + 1
        self.ID = Task.Counter
        print "Created thread: " + str(self.ID) + " duration:" + str(duration) + " loop: " + str(loop)
        pass
    
    def task(self):
        interval = random.randrange(0, self.duration) + 1
        print "\n thread: " + str(self.ID) + ". Sleeping for random duration: " + str(interval) + " second(s)"
        time.sleep(interval)
        print " thread: " + str(self.ID) + ". Exiting after sleeping for: " + str(interval) + " second(s)"
        time.sleep(1)

    def run(self):
        try :
            print "thread: " + str(self.ID)
            time.sleep(random.randrange(1,5))
            for i in range(0, self.loop):
                #print "thread: " + str(thread.ID) + ". iteration: " + str(i)
                with Task.lock:
                    self.task()
        except Exception as e:
            print "Exception in thread: " + str(self.ID)
            print str(e)
                
    @staticmethod
    def create_threads(count):
        Tasks = []
        for i in xrange(0, count):
            task = Task(random.randrange(1,3), random.randrange(1,5))
            Tasks.append(task)
            pass
        for i in xrange(0, count):
            task = Tasks[i]
            time.sleep(random.randrange(i,i+5))
            task.start()
        return Tasks
    

threads = Task.create_threads(random.randrange(3,10))

for thread in threads :
    print "Waiting for thread " + str(thread.ID) + " to complete"
    thread.join()
    print "Completed thread " + str(thread.ID)

''' 
    "thread" does not support join method. 
    So we need to wait for a random duration, 
    or do a polling to find if all threads complete 
'''

#time.sleep(100)

