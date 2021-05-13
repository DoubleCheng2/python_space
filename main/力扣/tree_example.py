# -*- coding: utf-8 -*-

# @Time : 2020-06-03 17:07

# @Author : Double 承（DC）

# @Site : 

# @File : tree_example.py

# @Software: PyCharm
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CreateTree:

    def __init__(self):
        self.Tree = None

    def setTree(self,l1 = None):

        if l1 != None:
            self.Tree = TreeNode(l1.pop(0))
            temp = [self.Tree]

            while len(l1) >0:
                tmp = temp.pop(0)
                data = l1.pop(0)
                if tmp.val != None :
                    tmp.left = TreeNode(data)
                    temp.append(tmp.left)
                if tmp.val != None and len(l1)>0:
                    data = l1.pop(0)
                    tmp.right = TreeNode(data)
                    temp.append(tmp.right)

    def addNode(self,data=None):
        """
        插入一个新节点，
        :param data:
        :return:
        """

    def getAllNode(self):
        """
        遍历树
        :return:
        """
        pass

    def getAreaNode(self,start,end):
        """
        遍历出一定范围的结果
        :param start:
        :param end:
        :return:
        """

    def getBeforeAll(self):
        """
        前序遍历，
        :return:
        """

    def getAfterAll(self):
        """
        后序遍历，
        :return:
        """

    def getCurrentAll(self):
        """
        中序遍历，
        :return:
        """

    def setTreeTwo(self):
        """
        树结构，排序
        :return:
        """

# 排序算法的次数比较

ac = CreateTree()
ac.setTree([10,5,-3,3,2,None,11,3,-2,None,1])

phone = [ac.Tree]

data = []

while len(phone)>0:
    tmp = phone.pop(0)
    data.append(tmp.val)
    print(tmp.val)
    if tmp.left !=None:
        phone.append(tmp.left)

    if tmp.right != None:
        phone.append(tmp.right)


print('--------------------',data)