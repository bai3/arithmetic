# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        max , index  = -1, 0
        # write code here
        for i in array:
            if index <= 0:
                index = i
            else:
                index += i
            if index > max:
                max = index
        return max