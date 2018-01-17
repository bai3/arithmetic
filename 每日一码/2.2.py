# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        output = []
        for i in range(1,tsum/2+1):
            for j in range(i,tsum/2+2):
                tmp = (j+i)*(j-i+1)/2
                if tmp == tsum:
                    output.append(range(i, j+1))
        return output
