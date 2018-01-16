# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        current = 1000
        tmp = [1]*2
        for i in array:
            a = tsum - i
            if a in array:
                now = a*i
                if now < current:
                    tmp[0] = min(a,i)
                    tmp[1] = max(a,i)
        if tmp == [1,1]:
            return []
        else:
            return tmp