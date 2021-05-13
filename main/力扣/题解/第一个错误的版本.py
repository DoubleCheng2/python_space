# -*- coding: utf-8 -*-

# @Time : 2021-04-02 16:12

# @Author : Double 承（DC）

# @Site : 

# @File : 第一个错误的版本.py

# @Software: PyCharm
import time

def isBadVersion(version):
    if version>=1702766719:
        return True
    else:return False

class Solution(object):

    def isBadVersion(self,n):
        return False

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """


        end = n
        start = 0
        while True:
            time.sleep(1)
            print(start,"------------", end, isBadVersion(end), 1702766719)
            if isBadVersion(end):
                if isBadVersion((start + end)//2):
                    end = (start + end)//2
                else:
                    if start + 1 == end:
                        return end
                    start = (start + end)//2



N = 1702766719
c = 2126753390
a = Solution()
v = a.firstBadVersion(c)
print(v)
