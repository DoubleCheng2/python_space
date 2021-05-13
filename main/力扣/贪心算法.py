# -*- coding: utf-8 -*-

# @Time : 2021-03-10 11:24

# @Author : Double 承（DC）

# @Site : 

# @File : 贪心算法.py

# @Software: PyCharm


def main():
    flowerbed = [1,0,0,0,1,0,0]
    # flowerbed = [0]
    n = 2


    lenf = len(flowerbed)
    m = 0
    for i in range(lenf):
        if lenf>1:
            if i==0:
                if flowerbed[0]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    m+=1
            elif i<lenf-1:
                if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    m+=1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    m += 1
        else:
            if flowerbed[0]==0:
                m+=1
    print(m)


class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lenf = len(s)
        index = 0
        num = 0
        for i in range(lenf):
            if lenf==1:
                if s=='1':
                    return True
                else:
                    return False
            else:
                if s[i]=='1':
                    if num==0:
                        index = i
                        num +=1
                    else:
                        if '0' in s[index:i+1]:
                            return False

        if num!=0:
            return True
        else:return False


input = "01"

a = Solution()
print(a.checkOnesSegment(input))
print(False == input.__contains__("01"))




