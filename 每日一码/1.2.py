# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        low = 0
        high = len(rotateArray) - 1
        while low <= high:
            mid = int((low + high) / 2)
            midval = rotateArray[mid]
            if midval > rotateArray[high]:
                low = mid + 1
            else:
                high = mid - 1
                if midval < rotateArray[mid - 1]:
                    print(midval)
                    return midval
