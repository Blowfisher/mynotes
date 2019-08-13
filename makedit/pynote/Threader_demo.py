#!/usr/bin/env python
#coding:utf-8

from threading import Thread
from queue import Queue
from time import sleep
def bar(x):
    sleep(5)
    print('Input is :',x)



print('Before')
t = Thread(target=bar,args=('Xiaoming',))

#print(t.isDaemon())
t.setDaemon(True)
t.start()
t.join(6)
print('After')