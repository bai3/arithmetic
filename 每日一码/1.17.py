# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        list1 = s[0:n]
        list2 = s[n:]
        return list2+list1
