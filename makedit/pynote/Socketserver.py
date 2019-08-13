#!/usr/bin/env python
#coding:utf-8

import socketserver
import time
import conf
dir_name = conf.dirname
class Myserver(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        #print('client is %s-%s-%s' %(self.request,self.server,self.client_address))
       #print('server is: %s'%(self.server))
       # print('client_address is: %s'%(self.client_address))
        #request.send(bytes("HTTP/1.1 200 OK\r\n\r\n", encoding='utf-8'))

        request = self.request
        request.send('Is ok!'.encode('utf-8'))
        data=request.recv(1024).decode('utf-8')
        command,filename,file_size = data.split(' ')
        file_recv = 0
        if command == 'get':
            pass
        if command == 'put':
            file_path = dir_name+filename
            with open(file_path,'wb+') as f:
                Flag = True
                while Flag:
                    if int(file_size) > file_recv:
                       data = request.recv(1024)
                       f.write(data)
                       file_recv += len(data)
                    else:
                        Flag = False




    def finish(self):
        pass

if __name__ == '__main__':
    IP_PORT = ('',9999)
    server = socketserver.ThreadingTCPServer(IP_PORT,Myserver)
    server.serve_forever()