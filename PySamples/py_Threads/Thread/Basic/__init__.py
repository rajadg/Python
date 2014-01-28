
import thread
import random
import time

class Task(object):
    
    lock = thread.allocate_lock()
    Counter = 0
    
    def __init__(self, duration, loop):
        self.duration = duration
        self.loop = loop
        Task.Counter = Task.Counter + 1
        self.ID = Task.Counter
        print "Created thread: " + str(self.ID)
        pass
    
    def task(self):
        interval = random.randrange(1, self.duration)
        print "\nthread: " + str(self.ID) + ". Sleeping for random duration: " + str(interval) + " second(s)"
        time.sleep(interval)
        print "thread: " + str(self.ID) + ". Exiting after sleeping for: " + str(interval) + " second(s)"
        time.sleep(1)

    @staticmethod
    def run(thread):
        try :
            print "thread: " + str(thread.ID) + "thread: " + str(thread) + "\n"
            time.sleep(random.randrange(1,5))
            for i in range(0, thread.loop):
                #print "thread: " + str(thread.ID) + ". iteration: " + str(i)
                with Task.lock:
                    thread.task()
        except Exception as e:
            print "Exception in thread: " + str(thread.ID)
            print str(e)
                
    @staticmethod
    def create_threads(count):
        Tasks = []
        threads = []
        for i in xrange(0, count):
            task = Task(i+2, count-i+2)
            Tasks.append(task)
            pass
        for i in xrange(0, count):
            task = Tasks[i]
            threads.append(thread.start_new(Task.run, (task,)))
        return threads
    

threads = Task.create_threads(3)

''' 
    "thread" does not support join method. 
    So we need to wait for a random duration, 
    or do a polling to find if all threads complete 
'''

time.sleep(100)

