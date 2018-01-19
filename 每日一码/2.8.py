# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        tmp = head = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                head.next = pHead2
                pHead2 = pHead2.next
            else:
                head.next = pHead1
                pHead1 = pHead1.next
            head=head.next
        head.next = pHead1 or pHead2
        return tmp.next