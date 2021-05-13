# -*- coding: utf-8 -*-

# @Time : 2021-03-22 15:24

# @Author : Double 承（DC）

# @Site : 

# @File : 旋转数组.py

# @Software: PyCharm


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # return nums[-k:]+(nums[:-k])
        while k>0:
            nums.insert(0,nums.pop(-1))
            k-=1
        return nums



A = Solution()

nums = [1,2,3,4,5,6,7]


k = 3
c = A.rotate(nums,k)
print(c)

# 旋转90度
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
new = []
n=4
for i in range(n):
    for j in range(n):
       new.append(matrix[n-j-1][i])
new_l = []
for i in range(n):
    new_l.append(new[i*4:i*4+4])
print(new_l)



