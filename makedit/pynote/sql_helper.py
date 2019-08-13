#!/usr/bin/env python
#coding:utf-8
import pymysql
import conf

account = dict(user = conf.user,host = conf.host,port = conf.port, passwd = conf.passwd)


class sql_helper(object):
    'This is a sql handler'

    def __init__(self):
        self.table = conf.table
        self.__account = account
        self.selecter = 'select * from '+ self.table + ' where name = %s'
        self.updater = 'update '+ self.table +' set password=md5(%s) where name=%s'
        self.inserter = 'insert into '+self.table+'(name,age,password) values(%s,%s,md5(%s))'
        self.deleter = 'delete from '+self.table+ ' where name=%s'
    def select(self,name):
        'Need two argument'
        conn = pymysql.connect(**self.__account)
        conn.select_db(conf.db)
        cur = conn.cursor()
        cur.execute(self.selecter,name)
        data=cur.fetchall()
        cur.close()
        conn.close()
        return data

    def update(self,password,name):
        item = (password,name)
        conn = pymysql.connect(**self.__account)
        conn.select_db(conf.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cur.execute(self.updater,item)
            conn.commit()
            Flag = 0
        except Exception as e:
            print(e)
            Flag = 1
        finally:
            cur.close()
            conn.close()
            if Flag == 1:
                return 1
            else:
                return 0

    def insert(self,name,age,password):
        item = (name,age,password)
        conn = pymysql.connect(**self.__account)
        conn.select_db(conf.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cur.execute(self.inserter,item)
            conn.commit()
            Flag = 0
        except Exception as e:
            print(e)
            Flag = 1
        finally:
            cur.close()
            conn.close()
            if Flag == 1:
                return 1
            else:
                return 0

    def delete(self,name):
        conn = pymysql.connect(**self.__account)
        conn.select_db(conf.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cur.execute(self.deleter,name)
            conn.commit()
            Flag = 0
        except Exception as e:
            print(e)
            Flag = 1
        finally:
            cur.close()
            conn.close()
            if Flag == 1:
                return 1
            else:
                return 0

    def insertmany(self,item):
        conn = pymysql.connect(**self.__account)
        conn.select_db(conf.db)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            cur.executemany(self.inserter,item)
            conn.commit()
            Flag = 0
        except Exception as e:
            print(e)
            Flag = 1
        finally:
            cur.close()
            conn.close()
            if Flag == 1:
                return 1
            else:
                return 0


if __name__ == '__main__':
    ts =sql_helper()
    item = [('liuying',29,'redhat'),('luoxiaofang',27,'redhat'),('Blowfisher',27,'redhat')]
    data= ts.insertmany(item)
    print(data)