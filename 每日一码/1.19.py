# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        tmp = []
        for i in numbers:
            if i in tmp:
                duplication[0]=i
                return True
            else:
                tmp.append(i)
        return False


