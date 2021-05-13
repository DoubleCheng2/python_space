# -*- coding: utf-8 -*-

# @Time : 2021-03-22 15:47

# @Author : Double 承（DC）

# @Site : 

# @File : 存在重复元素.py

# @Software: PyCharm

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_num = set(nums)
        return len(set_num)!=len(nums)



A = Solution()

nums = [1,2,3,4]


c = A.containsDuplicate(nums)
print(c)
