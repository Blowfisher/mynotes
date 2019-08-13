#!/usr/bin/env python
#coding:utf-8

import pickle



with open('D:/dump.txt','rb') as f:
    data = pickle.load(f)
    print(data)
