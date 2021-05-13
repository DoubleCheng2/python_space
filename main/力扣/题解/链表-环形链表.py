# -*- coding: utf-8 -*-

# @Time : 2021-03-24 14:57

# @Author : Double 承（DC）

# @Site : 

# @File : 链表-环形链表.py

# @Software: PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head!=None:
            all = [head]
            while head.next!=None:
                temp = head.next
                if temp in all:
                    return True
                else:
                    all.append(temp)
                    head=temp
            return False
        else:
            return False





















