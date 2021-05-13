# -*- coding: utf-8 -*-

# @Time : 2021-03-25 9:41

# @Author : Double 承（DC）

# @Site : 

# @File : 树-验证二叉搜索树.py

# @Software: PyCharm

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        [32,26,47,19,null,null,56,null,27]
        :type root: TreeNode
        :rtype: bool
        """
        left = True
        right = True
        if root!=None:

            if root.left!=None:
                if root.left.val<root.val:
                    if root.left.right!=None :
                        if root.left.right.val<root.val:
                            left = self.isValidBST(root.left)
                        else:
                            left = False
                    else:
                        left = True
                else:
                    left = False
            else:
                left = True


            if root.right!=None:
                if root.right.val>root.val:
                    if root.right.left!=None:
                        if root.right.left.val > root.val:
                            right = self.isValidBST(root.left)
                        else:
                            right = False
                    else:
                        right = True
                else:
                    right = False
            else:
                right = True
        return left and right








