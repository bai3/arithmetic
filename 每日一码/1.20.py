# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = A[:]
        for i in range(len(A)):
            sum = 1
            for n in range(len(A)):
                if n != i:
                    sum = sum*A[n]
            B[i] = sum
        return B