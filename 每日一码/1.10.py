# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if base == 0:
            return 0
        elif base == 1:
            return 1
        elif exponent == 0:
            return 1
        elif exponent == 1:
            return base
        else:
            return pow(base,exponent)


