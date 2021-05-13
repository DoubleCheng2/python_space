# -*- coding: utf-8 -*-

# @Time : 2020-09-17 11:15

# @Author : Double 承（DC）

# @Site : 

# @File : 多线程实例.py

# @Software: PyCharm

import time
import threading

"""
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：

线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。
"""


class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.num = 1
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()
        self.lock2.acquire()
        self.lock3.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber=0):
        """
        :type printNumber: method
        :rtype: void
        """
        i=1
        while i<=self.n:
            self.lock1.acquire()
            if self.num==1:
                print(0,end='')
                self.num = 0
            i+=1
            if i%2==1:
                self.lock2.release()
            else:
                self.lock3.release()

    def even(self, printNumber=0):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
            if i%2==0 :
                self.lock2.acquire()
                print(i,end='')
                self.num = 1
                self.lock1.release()

    def odd(self, printNumber=0):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
            if i%2==1:
                self.lock3.acquire()
                print(i,end='')
                self.num = 1
                self.lock1.release()


class ZeroEvenOdd1(object):
    def __init__(self, n):
        self.n = n
        self.num = 1
        self.semaphore = threading.Semaphore(1)
        self.semaphore2 = threading.Semaphore(0)
        self.semaphore3 = threading.Semaphore(0)
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber=0):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
            self.semaphore.acquire()
            print(0,end='')
            if i%2==0:
                self.semaphore2.release()
            else:
                self.semaphore3.release()

    def even(self, printNumber=0):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
            if i%2==0 :
                self.semaphore2.acquire()
                print(i,end='')
                self.num = 1
                self.semaphore.release()

    def odd(self, printNumber=0):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1,self.n+1):
            if i%2==1:
                self.semaphore3.acquire()
                print(i,end='')
                self.num = 1
                self.semaphore.release()

# zeo = ZeroEvenOdd1(10)
#
#
# threading.Thread(target=zeo.even,name='even').start()
# threading.Thread(target=zeo.zero,name='zero').start()
# threading.Thread(target=zeo.odd,name='odd').start()



"""
请你实现一个有四个线程的多线程版  FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用：

线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。
线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。
线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。
线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。
"""

class FizzBuzz1(object):

    def __init__(self, n):
        self.n = n
        self._num = 1
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()
        self.lock4 = threading.Lock()

        self.lock1.acquire()
        self.lock2.acquire()
        self.lock3.acquire()

    # printFizz() outputs "fizz"
    def fizz(self):
        """
        :type printFizz: method
        :rtype: void
        """
        while self._num <= self.n:
            if self._num % 3 == 0 and self._num % 5 != 0 and self._num <= self.n:
                self.lock1.acquire()
                print("fizz",end=',')
                self.lock4.release()


    # printBuzz() outputs "buzz"
    def buzz(self):
        """
        :type printBuzz: method
        :rtype: void
        """
        while self._num <= self.n:
            if self._num % 3 != 0 and self._num % 5 == 0 and self._num <= self.n:
                print("buzzssss")
                self.lock2.acquire()
                print("buzz", end=',')
                self.lock4.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        while self._num <= self.n:
            if self._num%15==0 and self._num <= self.n:
                print("fizzssss")
                self.lock3.acquire()
                print("fizzbuzz", end=',')
                self.lock4.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self):
        """
        :type printNumber: method
        :rtype: void
        """
        while self._num <= self.n:
            if self._num%3 !=0 and self._num%5!=0 and self._num <= self.n:
                self.lock4.acquire()
                print(self._num, end=',')
                self.lock4.release()
            elif self._num % 3 == 0 and self._num % 5 != 0 and self._num <= self.n:
                self.lock4.acquire()
                self.lock1.release()
            elif self._num % 3 != 0 and self._num % 5 == 0 and self._num <= self.n:
                self.lock4.acquire()
                self.lock2.release()
            elif self._num %15==0 and self._num <= self.n:
                self.lock4.acquire()
                self.lock3.release()
            self._num += 1


# fizz = FizzBuzz1(15)
#
# threading.Thread(target=fizz.number,name='number').start()
# threading.Thread(target=fizz.fizz,name='fizz').start()
# threading.Thread(target=fizz.buzz,name='buzz').start()
# threading.Thread(target=fizz.fizzbuzz,name='fizzbuzz').start()


class FizzBuzz:

    def __init__(self, n: int):
        self.n = n
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()
        self.lock4 = threading.Lock()

        self.lock2.acquire()
        self.lock4.acquire()
        self.lock3.acquire()

    # printFizz() outputs "fizz"
    def fizz(self) -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.lock2.acquire()
                print("fizz,")
                self.lock1.release()


                # printBuzz() outputs "buzz"

    def buzz(self) -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                self.lock3.acquire()
                print('buzz,')
                self.lock1.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self,) -> None:
        for i in range(1, self.n + 1):
            if i % 15 == 0:
                self.lock4.acquire()
                print('fizzbuzz,')
                self.lock1.release()
                # printNumber(x) outputs "x", where x is an integer.

    def number(self) -> None:
        for i in range(1, self.n + 1):
            # self.mute_num.acquire()
            if i % 3 != 0 and i % 5 != 0:
                self.lock1.acquire()
                print(i)
                self.lock1.release()
            elif i % 3 == 0 and i % 5 != 0:
                self.lock1.acquire()
                self.lock2.release()
            elif i % 5 == 0 and i % 3 != 0:
                self.lock1.acquire()
                self.lock3.release()
            elif i % 15 == 0:
                self.lock1.acquire()
                self.lock4.release()


class FizzBuzz2:

    def __init__(self, n: int):
        self.n = n
        # 信号量
        self.semaphore = threading.Semaphore(1)
        self.num = 1

    # printFizz() outputs "fizz"
    def fizz(self) -> None:
        while self.num <= self.n:
            self.semaphore.acquire()
            if self.num % 3 == 0 and self.num % 5 != 0 and self.num <= self.n:
                print("fizz",end=',')
                self.num += 1
            self.semaphore.release()

    def buzz(self) -> None:
        while self.num <= self.n:
            self.semaphore.acquire()
            if self.num % 3 != 0 and self.num % 5 == 0 and self.num <= self.n:
                print('buzz',end=',')
                self.num += 1
            self.semaphore.release()

    def fizzbuzz(self,) -> None:
        while self.num<=self.n:
            self.semaphore.acquire()
            if self.num % 15 == 0 and self.num <= self.n:
                print('fizzbuzz',end=',')
                self.num += 1
            self.semaphore.release()

    def number(self) -> None:
        while self.num <= self.n:
            self.semaphore.acquire()
            if self.num % 3 != 0 and self.num % 5 != 0 and self.num <= self.n:
                print(self.num,end=',')
                self.num +=1
            self.semaphore.release()


fizz = FizzBuzz2(15)

threading.Thread(target=fizz.number,name='number').start()
threading.Thread(target=fizz.fizz,name='fizz').start()
threading.Thread(target=fizz.buzz,name='buzz').start()
threading.Thread(target=fizz.fizzbuzz,name='fizzbuzz').start()
