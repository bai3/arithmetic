# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        list1 = []
        list2 = []
        for n in array:
            if n % 2 != 0:
                list1.append(n)
            else:
                list2.append(n)
        list1.extend(list2)
        return list1
