# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        index = 0
        if len(s) == 1:
            return s
        elif len(s) == 0:
            return -1
        else:
            for i in s:
                if s.count(i) == 1:
                    return index
                index +=1