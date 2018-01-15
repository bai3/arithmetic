# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array) == 2:
            return array
        else:
            list = []
            for i in array:
                if array.count(i) == 1:
                    list.append(i)
            return list