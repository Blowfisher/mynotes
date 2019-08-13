#!/usr/bin/env python
#coding:utf-8

import socketserver
import time
import conf,os
dir_name = 'E:/Code/'


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
        try:
            command, filename, file_size = data.split(' ')
        except:
            command,filename = data.split(' ')

        if command == 'get' or command == 'GET':
            command, filename = data.split(' ')
            file_path = os.path.join(dir_name,filename)
            try:
                file_size = os.path.getsize(file_path)
                file_size1 = str(file_size).encode('utf-8')
                request.send(file_size1)
                with open(file_path, 'rb') as f:
                    Flag = True
                    file_send = 0
                    while Flag:
                        if file_size > file_send:
                            data = f.read(1024)
                            request.send(data)
                            file_send += len(data)
                        else:
                            Flag = False
                            print('Success transfer...')
            except Exception as e:
                print(e)
                return 1

        if command == 'put' or command == 'PUT':
            command, filename, file_size = data.split(' ')
            file_path = dir_name+filename
            with open(file_path,'wb+') as f:
                file_recv = 0
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