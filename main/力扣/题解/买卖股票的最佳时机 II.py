# -*- coding: utf-8 -*-

# @Time : 2021-03-22 14:15

# @Author : Double 承（DC）

# @Site : 

# @File : 买卖股票的最佳时机 II.py

# @Software: PyCharm


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_p = len(prices)
        total = 0
        start = 0

        for i in range(len_p):
            if i+1<len_p:
                if prices[i+1] < prices[i]:
                    total = prices[i]-prices[start] + total
                    start = i+1
            else:
                total = prices[i] - prices[start] + total

        return total


A = Solution()

b = [7,1,5,3,6,4]
# b = [1,2,3,4,5]
c = A.maxProfit(b)
print(c)

