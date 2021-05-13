# -*- coding: utf-8 -*-

# @Time : 2021-05-08 16:33

# @Author : Double 承（DC）

# @Site : 

# @File : 树-对称二叉树.py

# @Software: PyCharm

class TreeNode(object):
    # [1,2,2,null,3,null,3]
    # [1,2,2,3,4,4,3]
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isSymmetric(self, root):
        """
        每一层的值正反一样
        :type root: TreeNode  [1,2,2,3,4,4,3]
        :rtype: bool
        """

        queue = [root]

        while queue:
            next_queue = []
            layer = []
            for node in queue:
                # 数值为None
                if not node:
                    layer.append(None)
                    continue
                next_queue.append(node.left)
                next_queue.append(node.right)
                layer.append(node.val)
            if layer!=layer[::-1]:
                return False
            queue = next_queue
        return True

    def isSymmetric2(self,root):
        """
        每一层的值正反一样
        :param root:
        :return:
        """
        if not root:
            return True
        else:
            def compareRoot(root1,root2):
                if not root1 and not root2:
                    return True
                if not root1 or not root2:
                    return False
                return root1.val==root2.val and compareRoot(root1.left,root2.right) and compareRoot(root1.right,root2.left)

            return compareRoot(root.left, root.right)






root = [1,None,2,3]

root1 = TreeNode(val=1,right=TreeNode(val=2,left=TreeNode(val=3)))

solution = Solution()
values = solution.isSymmetric(root1)
print(values)






















