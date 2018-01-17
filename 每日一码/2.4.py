# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        list = s.split(" ")
        return ' '.join(list[::-1])