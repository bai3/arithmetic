# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        half = len(numbers) / 2
        if not numbers:
            return 0
        elif len(numbers) == 1:
            return numbers[0]
        else:
            b = {}
            for x in numbers:
                if x in b:
                    b[x] += 1
                    if b[x] > half:
                        return x
                else:
                    b[x] = 1
            return 0