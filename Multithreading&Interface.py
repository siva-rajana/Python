#                   *********** Multithreading ***********

#Multasking:- Multithreading is two types:-1.Process based multitasking 2.Thread based multitasking.
'''
1.Process based multitasking:- In this each task is separate independant process.
                           Ex:-1.Typing a python program in python editing
                                 Listening audio songs in same system,Download new songs from internet.

2.Thread Based Multitasking:- In this Each task is the independent part of the same program.
                              A flow of Execution is considered as a thread.it is Python Object.For every thread independent job is available. 

'''
'''
from threading import thread
import time
t1=time.time()
for i in range(1,501):
    print(i,"python")
for i in range(1,501):
    print(i,"java")
t2=time.time()
print("the time taken is",(t2-t1))
'''

#Q.)Write a program to print a floew of execution using thread?(single thread).
'''
from threading import thread
import time
def fun1():
    for i in range(1,501):
           print(i,"python")
def fun2():
    for i in range(1,501):
           print(i,"java")

t1=thread(target=fun2)
t1.start()
'''
#Q.)Write a program to print a floew of execution using thread?(single thread).
'''
from threading import thread
import time
def fun1():
    for i in range(1,501):
           print(i,"python")
def fun2():
    for i in range(1,501):
           print(i,"java")
a1=time.time()
t1=thread(target=fun1)
t1=thread(target=fun2)
t1.start()
t2.star()
t1.join()
t2.join()
a2=time.time()
print("the time taken is",(a2-a1))
'''

#           *********** Process Sleep *************
'''
import time
t1=time.time()
for i in range(1,11):
    print(i,"python")
    time.sleep(2)
t2=time.time()
print()
print((t2-t1))
'''

#            **************** Interface ******************

#Interface:- A class can contain any no.of methods if in that all the methods are dummy methods then that class is called "Interface".


from abc import ABC
class myinter:
    def connect(self):
        pass
    def disconnect(self):
        pass
class oracle(myinter):
    def connect(self):
        print("I am connecting to oracle")
    def disconnect(self):
        print("i am disconnecting oracle")
class mysql(myinter):
    def connect(self):
        print("I am connecting to mysql")
    def disconnect(self):
        print("i am disconnecting mysql")
class sybase(myinter):
    def connect(self):
        print("I am connecting to sybase")
    def disconnect(self):
        print("i am disconnecting sybase")
o=oracle()
m=mysql()
s=sybase()
o.connect()
o.disconnect()
s.connect()





























