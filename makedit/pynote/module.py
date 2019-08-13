#!/usr/bin/env python
#coding:utf-8
import pymysql,conf


#account = dict(user = 'pig',host = '192.168.10.11',port = 3306 ,passwd = 'redhat',db = 'lister')
#conn = pymysql.connect(**account)
class Db_helper(object):
    "MySQL dcl s"

    def __init__(self):
        self.__account = conf.account

    def select(self,item):
        self.conn = pymysql.connect(**self.__account)
        self.cur = self.conn.cursor()
        self.sql = 'select * from %s where name=%s;'
        self.item = item
        self.cur.execute(self.sql,(self.item))
        data = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return data
    def insert(self,*item):
        self.item = item
        self.conn = pymysql.connect(**self.__account)
        self.cur = self.conn.cursor()
        self.sql = 'insert into message (name,age)values(%s,%s);'
        data = self.cur.executemany(self.sql,(self.item))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return data
    def update(self,*item):
        self.conn = pymysql.connect(**self.__account)
        self.cur = self.conn.cursor()
        if item == True:
            data = self.select(item)
            print(data)
        else:
            data = input('name:')
        self.sql = 'update message set name=%s ;'
        self.item = item
        data = self.cur.executemany(self.sql,(self.item))
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        return data



a = Db_helper()
b = ['message','liuying']
data = a.select(b)
print(data)
>>>>>>> Stashed changes
