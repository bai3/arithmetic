import itertools
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        s = itertools.permutations(ss)
        result = []
        for i in s:
            result.append(''.join(i))
        result = list(set(result))
        result.sort()
        return result
