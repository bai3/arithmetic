# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list = []
        p1 = pHead1
        p2 = pHead2
        while p1 != None:
            list.append(p1.val)
            p1 = p1.next
        while p2 != None:
            if p2.val in list:
                return p2
            else:
                p2 = p2.next