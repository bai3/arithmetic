# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n == 1 or n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 0:
            return 0
        else:
            b = 1
            c = 2
            for i in range(4, n+1):
                c = c + b
                b = c - b
            return c