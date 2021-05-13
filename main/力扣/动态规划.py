# -*- coding: utf-8 -*-

# @Time : 2020-12-23 10:50

# @Author : Double 承（DC）

# @Site : 

# @File : 动态规划.py

# @Software: PyCharm

class Solution(object):
    def maximumProduct(self, nums):
        """
        取三个数乘积最大值的值
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])

    def maxSubArray(self, nums):
        """
        最大子序和
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for i in range(1,len(nums)):

            # 表示起始index
            a = i
            # 表示最大值
            v = 0
            t = max([t,t+nums[i],nums[i]])




if __name__ == '__main__':

    s =  [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    a = sol.maximumProduct(s)
    print(a)




