#/usr/bin/env python
#coding:utf-8
import socket
import os
import re


dir_name = 'G:/Coder/'
server_ip_port = ('172.16.109.151',9999)


class file_handler(object):
    def __init__(self,server_ip_port):
            self.client = socket.socket()
            self.client.connect(server_ip_port)
            print(self.client.recv(1024))

    def file_input(self):
        # 需要处理的文件 做预处理
        print('Useage:Command(get/put)  file')
        self.input = input('请输入需要上传的文件:')
        command,file_path = re.split(r'\s+',self.input)
        base_name = os.path.basename(file_path)
        return command,file_path,base_name


    def file_transfer(self,command,file_path,base_name):
        '文件上传下载操作'
        print('Start transfer...')
        if command == 'put' or command == 'PUT':
            try:
                file_size = os.stat(file_path).st_size
            except Exception as e:
                print(e)
                exit(2)

            file_info = ' '.join([command, base_name, str(file_size)])
            file_info = bytes(file_info, encoding='utf-8')
            self.client.send(file_info)
            with open(file_path, 'rb') as f:
                Flag = True
                file_send = 0
                while Flag:
                    if file_size > file_send:
                        data = f.read(1024)
                        self.client.send(data)
                        file_send += len(data)
                    else:
                        Flag = False
                        print('Success transfer...')


        if command == 'get' or command == 'GET':
            file_info = ' '.join([command, base_name])
            file_info = bytes(file_info, encoding='utf-8')
            file_path = os.path.join(dir_name, base_name)
            self.client.send(file_info)
            file_size = (self.client.recv(1024)).decode('utf-8')
            with open(file_path, 'wb+') as f:
                file_recv = 0
                Flag = True
                while Flag:
                    if int(file_size) > file_recv:
                        data = self.client.recv(1024)
                        f.write(data)
                        file_recv += len(data)
                    else:
                        Flag = False
                        print('Success transfer...')
                        return 3



if __name__ == "__main__":
    test = file_handler(server_ip_port)
    command, file_path, base_name=test.file_input()
    test.file_transfer(command,file_path,base_name)




