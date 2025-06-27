                        # Multithreating

for i in range(65,91):
    print(i)



from threading import *
from time import *
def display():
    for i in range(65,91):
        print(chr(i))
        sleep(1)

t=Thread(target=display,name = 'Alphabet')
t.start()
for i in range(65,91):
    print(i)
    sleep(1)
t.join()      # The order it get executed is not always same



from threading import *
from time import *

class Alphabets(Thread):
    def run(self):
        for i in range(65,91):
            print(chr(i))
            sleep(1)

t=Alphabets()
t.start()
for i in range(65,91):
    print(i)
    sleep(1)
t.join() 




# Thread Synchronisation
from threading import *         # Race Condition

def display(str1):
    for i in str1:
        print(i)

t1 = Thread(target=display,args=('HELLO WORLD',))
t2 = Thread(target=display,args=('you are welcome',))
                                            
t1.start()
t2.start()

t1.join()
t2.join()

# Mutex:
from threading import *         

def display(str1):
    l.acquire()
    for i in str1:
        print(i)
    l.release()

l = Lock()
t1 = Thread(target=display,args=('HELLO WORLD',))
t2 = Thread(target=display,args=('you are welcome',))
                                            
t1.start()
t2.start()

t1.join()
t2.join()



# Semaphora:
from threading import *         

def display(str1):
    l.acquire()
    for i in str1:
        print(i)
        
    l.release()

l = Semaphore(2)
t1 = Thread(target=display,args=('HELLO WORLD',))
t2 = Thread(target=display,args=('you are welcome',))
t3 = Thread(target=display,args=('0123456789',))
                                            
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()



# Interprocess Communication:
from threading import *
from time import *
class mydata:
    def __init__(self):
        self.data = 0
        self.flag = False
        self.lock = Lock()
    
    def put(self,d):            # This method is used by consumer
        while self.flag != False:
            pass
        self.lock.acquire()
        self.data = d
        self.flag = True
        self.lock.release()
        sleep(1)
    
    def get(self):               #  This method is used by consumer
        while self.flag != True:
            pass
        self.lock.acquire()
        x = self.data
        self.flag = False
        self.lock.release()
        sleep(1)
        return x
        
def producer(data):
    i=1
    while True:
        data.put(i)
        print('Producer:',i)
        i += 1

def consumer(data):
    while True:
        x = data.get()
        print('Consumer:',x)
        
data = mydata()
d1 = Thread(target=lambda:producer(data))
d2 = Thread(target=lambda:consumer(data))

d1.start()# Here output is mixed due to race conditions and very fast due to infinite loop
        # Now make the code little slow to write sleep() in side producer and consumer method:
        # we can also make the code little slow to write sleep() in side put() and get() method:
d2.start()

d1.join()
d2.join()  

       

# Inter-process Communication Using Conditions:
      # Main change in this is flag and loop is not there
from threading import *
from time import *
class Mydata:
    def __init__(self):
        self.data = 0
        self.cv = Condition()
        
    
    def put(self,d):           # This method is used by consumer
#         while self.flag != False:   # Loop for waiting is converted in to wait method
#             pass
#         self.lock.acquire()
        self.cv.acquire()
        self.cv.wait(timeout=0)  
        self.data = d
        self.cv.notify()
        self.cv.release()
        sleep(1)
    
    def get(self):               #  This method is used by consumer
#         while self.flag != True:    # Loop for waiting is converted in to wait method
#             pass
#         self.lock.acquire()

        self.cv.acquire()
        self.cv.wait(timeout=0)
        x = self.data
        self.cv.notify()
        self.cv.release()
        sleep(1)
        return x
        
def producer(data):
    i=1
    while True:
        data.put(i)
        print('Producer:',i)
        i += 1

def consumer(data):
    while True:
        x = data.get()
        print('Consumer:',x)
        
data = Mydata()
d1 = Thread(target=lambda:producer(data))
d2 = Thread(target=lambda:consumer(data))

d1.start()
d2.start()

d1.join()
d2.join() 



# Inter-process Communication Using Queue:
from threading import *
from time import *
from queue import *

'''# class Mydata:
#     def __init__(self):
#         self.data = 0
#         self.cv = Condition()
        
    
#     def put(self,d):           # This method is used by consumer
# #         while self.flag != False:   # Loop for waiting is converted in to wait method
# #             pass
# #         self.lock.acquire()
#         self.cv.acquire()
#         self.cv.wait(timeout=0)  
#         self.data = d
#         self.cv.notify()
#         self.cv.release()
#         sleep(1)
    
#     def get(self):               #  This method is used by consumer
# #         while self.flag != True:    # Loop for waiting is converted in to wait method
# #             pass
# #         self.lock.acquire()

#         self.cv.acquire()
#         self.cv.wait(timeout=0)
#         x = self.data
#         self.cv.notify()
#         self.cv.release()
#         sleep(1)
#         return x'''
# Avobe is only for example:

q = Queue()   # It behave lke mydata()
        
def producer(que):
    i=1
    while True:
        que.put(i)
        print('Producer:',i)
        sleep(1)
        i += 1
        # sleep(1)

def consumer(que):
    while True:
        x = que.get()
        print('Consumer:',x)
        sleep(1)
        

d1 = Thread(target=lambda:producer(q))
d2 = Thread(target=lambda:consumer(q))

d1.start()
d2.start()

d1.join()
d2.join() 


            # The End: (We can use anyone of the three method)