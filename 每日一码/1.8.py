# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        tinput.sort()
        b = tinput[:k]
        return b