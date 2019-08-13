#!/usr/bin/env python
#coding:utf-8

import socket,time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',9999))
s.listen(5)

while True:
    print('Waiting Connection...')
    conn,address = s.accept()
    print('From ',address)
    data= conn.recv(1024)
    conn.send(bytes("HTTP/1.1 200 OK\r\n\r\n",encoding='utf-8'))
    conn.sendall(data)
    conn.close()

