# -*- coding:utf-8 -*-
import operator
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        num = map(str, numbers)
        num.sort(lambda x,y:cmp(x+y,y+x))
        return ''.join(num)

