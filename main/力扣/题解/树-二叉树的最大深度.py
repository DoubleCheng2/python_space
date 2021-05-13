# -*- coding: utf-8 -*-

# @Time : 2021-03-25 9:40

# @Author : Double 承（DC）

# @Site : 

# @File : 树-二叉树的最大深度.py

# @Software: PyCharm

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root!=None:
            i = 1
            j = 1
            if root.left!=None:
                i += self.maxDepth(root.left)
            if root.right!=None:
                j += self.maxDepth(root.right)
            return max(i,j)
        else:
            return 0























