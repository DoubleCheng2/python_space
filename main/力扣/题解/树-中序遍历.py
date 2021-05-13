# -*- coding: utf-8 -*-

# @Time : 2021-05-07 16:45

# @Author : Double 承（DC）

# @Site : 

# @File : 树-中序遍历.py

# @Software: PyCharm
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution(object):

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root!=None:
            line = [root.val]
            if root.left !=None:
                temp = self.preorderTraversal(root.left)
                temp.extend(line)
                line = temp
            if root.right!=None:
                line.extend(self.preorderTraversal(root.right))
            return line
        else:
            return []



root = [1,None,2,3]

root1 = TreeNode(val=1,right=TreeNode(val=2,left=TreeNode(val=3)))

solution = Solution()
values = solution.preorderTraversal(root1)
print(values)

