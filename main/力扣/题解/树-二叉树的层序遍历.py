# -*- coding: utf-8 -*-

# @Time : 2021-03-26 10:19

# @Author : Double 承（DC）

# @Site : 

# @File : 树-二叉树的层序遍历.py

# @Software: PyCharm
import time


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root!=None:
            temp = [root]
            value = []
            while temp!=[]:
                tree_list = []
                tree_val = []
                for line in temp:
                    tree_val.append(line.val)
                    if line.left!=None:
                        tree_list.append(line.left)
                    if line.right!=None:
                        tree_list.append(line.right)
                value.append(tree_val)
                time.sleep(1)
                temp = tree_list

            return value
        else:
            return []


list1 = [3,9,20,None,None,15,7]

root = TreeNode(val=3,left=TreeNode(val=9),right=TreeNode(val=20,left=TreeNode(val=15),right=TreeNode(val=7)))

s = Solution()

d = s.levelOrder(root)
print(d)



























