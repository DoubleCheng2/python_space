# -*- coding: utf-8 -*-

# @Time : 2020-09-10 10:03

# @Author : Double 承（DC）

# @Site : 

# @File : 线程大师.py

# @Software: PyCharm
import threading
import time
from datetime import datetime
from queue import Queue

class Foo(object):
    def __init__(self):
        self.step = 0
        pass

    def first(self):
        """
        :type printFirst: method
        :rtype: void
        """
        self.step += 1
        # printFirst() outputs "first". Do not change or remove this line.
        print('first')

    def second(self):
        """
        :type printSecond: method
        :rtype: void
        """
        while self.step != 1:
            pass
        self.step += 1

        # printSecond() outputs "second". Do not change or remove this line.
        print('second')

    def third(self):
        """
        :type printThird: method
        :rtype: void
        """
        while self.step != 2:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        print('third')


class ThreadPoolTest(object):

    def __init__(self,n):
        self._que = Queue()
        for i in range(n):
            threading.Thread(target=self.worker,name="线程%d"%i)

    def worker(self):
        """
        定义线程执行的任务
        :return:
        """
        while True:
            func,args,kwargs = self._que.get()
            func()
            break

    def apply_async(self,target,args=(),kwargs={}):
        """
        给que传入值
        :param target:
        :param args:
        :param kwargs:
        :return:
        """
        self._que.put((target,args,kwargs))


from multiprocessing.pool import ThreadPool

def hello(arg):
    print("start")
    time.sleep(1)
    print("end")
    print(arg)

pool = ThreadPool(3)
for i in range(10):
    pool.apply_async(hello,args=('xyz',))

pool.close()
pool.join() # 在join之前必须要close，这样就不允许再提交任务了

# 池的其他操作
# 操作一： close - 关闭提交通道，不允许再提交任务
# 操作二： terminate - 中止进程池，中止所有任务


if __name__ == '__main__':

    foo = Foo()
    th = []
    c = threading.Thread(target=foo.third,name='third')
    th.append(c)
    b = threading.Thread(target=foo.second,name='second')
    th.append(b)
    a = threading.Thread(target=foo.first,name='first')
    th.append(a)
    for i in th:
        i.start()
    c.join()
    # for j in th:
    #     j.join()
    print("end")

