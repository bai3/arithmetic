# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number <= 0:
            return 0
        elif number <= 2:
            return number
        else:
            b = 1
            c = 2
            for i in range(3, number+1):
                c = c + b
                b = c - b
            return c