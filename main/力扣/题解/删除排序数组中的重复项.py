# -*- coding: utf-8 -*-

# @Time : 2021-03-22 14:15

# @Author : Double 承（DC）

# @Site : 

# @File : 删除排序数组中的重复项.py

# @Software: PyCharm
# 删除排序数组中的重复项
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i<len(nums):
            if nums[i+1] in nums[:i+1]:
                nums.pop(i+1)
            else:
                i+=1
        return len(nums),nums


A = Solution()

b = [0,0,1,1,1,2,2,3,3,4]
c = A.removeDuplicates(b)
print(c)




