# -*- coding: utf-8 -*-

# @Time : 2021-05-11 11:39

# @Author : Double 承（DC）

# @Site : https://blog.csdn.net/ZT7524/article/details/103464673

# @File : 树-创建树.py

# @Software: PyCharm

# -*- coding:utf-8 -*-

'二叉树结点类'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'列表创建二叉树'


def listCreatTree(root1, llist, i):
    if i < len(llist):
        if llist[i] == None:
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要

    return root1


if __name__ == '__main__':
    index = [0,1,2,3   ,4,   5,6,7   ,8   ,9,10]
    llist = [1,2,3,None,4,None,5,None,None,6,None]
    root = listCreatTree(None, llist, 0)
    print(root)
    #p = root
    # print(".............................")
    # preOrderBT(root)
    # print()
    # midOrdBT(root)
    # print(root.val)
    # while root






