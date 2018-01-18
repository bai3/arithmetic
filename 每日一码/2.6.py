# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        list = []
        while head != None:
            list.append(head)
            head=head.next
        if k > len(list) or k < 1:
            return
        return list[-k]