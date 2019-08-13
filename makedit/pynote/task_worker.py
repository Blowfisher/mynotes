#!/usr/bin/env python
#coding:utf-8

import time,sys,Queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
        pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '192.168.5.5'

print 'Connect to server %s...'%(server_addr)

m = QueueManager(address=(server_addr,5000),authkey=b'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
        try:
                n = task.get(timeout=1)
                print 'Run task %d * %d...' %(n,n)
                r = '%d * %d = %d' %(n,n,n*n)
                time.sleep(1)
                result.put(r)
        except Queue.Empty:
                print 'Task queue is empty.'

print 'Worke exit.'

