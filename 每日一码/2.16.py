# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers) < 5:
            return False
        numbers.sort()
        count = 0
        for i in numbers:
            if i == 0:
                count += 1
                continue
            else:
                break
        numbers = numbers[count:]
        if numbers[-1] - numbers[0] < 5 and len(numbers) == len(set(numbers)):
            return True
