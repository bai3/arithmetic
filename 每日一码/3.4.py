# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return None
        pre = None
        cur = pHead
        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    if not pre:
                        pHead = cur.next
                        cur = cur.next
                    else:
                        cur = cur.next
                        pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return pHead