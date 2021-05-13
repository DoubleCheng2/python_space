# -*- coding: utf-8 -*-

# @Time : 2021-02-01 16:32

# @Author : Double 承（DC）

# @Site : 

# @File : 队列.py

# @Software: PyCharm

# 3、队列
def realizationQueue():
    print("---------------------------------------------队列")
    from queue import Queue
    Q1 = Queue()
    for i in range(30):
        Q1.put(i)
    for i in range(30):
        print(Q1.get(),end=',')


