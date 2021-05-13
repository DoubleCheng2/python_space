# -*- coding: utf-8 -*-

# @Time : 2021-02-01 16:31

# @Author : Double 承（DC）

# @Site : 

# @File : 栈.py

# @Software: PyCharm
# 2、栈
def realizationStack():
    print("---------------------------------------------栈")
    class Stack:

        def __init__(self):
            self._sList = []

        def put(self,element):
            self._sList.append(element)

        def get(self):
            if len(self._sList)!=0:
                return self._sList.pop()
            else:return None

    stack = Stack()
    for i in range(30):
        stack.put(i)
    for i in range(30):
        print(stack.get(),end=',')


