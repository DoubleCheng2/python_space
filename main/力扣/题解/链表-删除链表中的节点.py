# -*- coding: utf-8 -*-

# @Time : 2021-03-23 9:09

# @Author : Double 承（DC）

# @Site : 

# @File : 链表-删除链表中的节点.py

# @Software: PyCharm


# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        list_new = [head.val]
        while head.next != None:
            list_new.append(head.next.val)
            head = head.next

        new_head = ListNode()
        new_head.val = list_new.pop(0)
        while list_new != []:
            temp = ListNode()
            temp.val = list_new.pop(0)
            temp.next = new_head
            new_head = temp
        return new_head


A = Solution()







