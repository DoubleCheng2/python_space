# -*- coding: utf-8 -*-

# @Time : 2021-05-07 17:38

# @Author : Double 承（DC）

# @Site : 

# @File : 树-后序遍历.py

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
            else:
                temp = None

            if root.right!=None:
                temp2 = self.preorderTraversal(root.right)
            else:
                temp2 = None

            if temp:
                if temp2:
                    temp.extend(temp2)
                    temp.extend(line)
                else:
                    temp.extend(line)
                line = temp
            else:
                if temp2:
                    temp2.extend(line)
                    line = temp2

            return line
        else:
            return []



root = [1,None,2,3]

root1 = TreeNode(val=1,right=TreeNode(val=2,left=TreeNode(val=3)))

solution = Solution()
values = solution.preorderTraversal(root1)
print(values)



