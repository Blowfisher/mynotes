#coding:utf8

import os
import sys
import json
import subprocess
from subprocess import PIPE,Popen

username = ''
password = ''


# 当crontab mongodb数据维护 对应的服务端口 更改时此处需要修改
def Monstart(port):
    if port == 27017:
        Start_cmd = """sudo /usr/bin/mongod -f /etc/mongod.conf """
        second_cmd = """sudo /bin/netstat -tnlp|grep %s """%port
        start_tmp = Popen(Start_cmd,shell=True,stdout=PIPE,stderr=PIPE)    
        second_tmp = Popen(second_cmd,stderr=PIPE,stdout=PIPE,shell=True).stderr.read() == ''
        if cmd_tmp.stderr.read() == '' and type(second_tmp.stdout.read()) == str:
            return 1
    if port == 4444:
        Start_cmd = """sudo /usr/bin/mongod --dbpath=/data/mongodb3 --port 4444 --logpath=/data/mongodb3/logs --fork"""
        second_cmd = """ ps aux|grep mongo|grep %s"""%port
        start_tmp = Popen(Start_cmd,shell=True,stdout=PIPE,stderr=PIPE)
        if cmd_tmp.stderr.read() == '' and  type(second_tmp.stdout.read()) == str:
            return 1
        
# LLD 自动发现端口    
if sys.argv[1] == "list":
    Command  = """sudo /bin/netstat -tnlp|grep mongo |awk '{print $4}'|cut -d: -f2"""
    temp = subprocess.Popen(Command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    Flag = True
    data_list = []
    while Flag:
        port = temp.stdout.readline()    
        if port == '':
            Flag = False
        else: 
            data = int(port.strip('\n'))
            data_list.append({"{#MOPORT}":data})
    result = json.dumps({"data":data_list},indent=7,sort_keys=True,separators=(",",":"))
    print result
#获取键值对
elif type(int(sys.argv[1])) == int:
    ip = '172.16.2.38:'+sys.argv[1]
    data="/usr/bin/mongo --quiet  %s --eval 'JSON.stringify(db.serverStatus())'" %ip
    temp = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
    result = json.loads(temp,encoding="utf-8")

    if result["ok"] != 1:
        Monstart(sys.argv[1])

    try:
        for i in sys.argv[2:]:
            result = result[i]
    except Exception as e:
        print e
        exit(1)
    if type(result) is dict:
        Key = result.keys()
        print result[Key[0]]
    else:
        print result
else:
    print('参数错误...')


