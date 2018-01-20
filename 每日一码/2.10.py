# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        zheng = 1
        l = len(s)
        result = 0
        if l == 0:
            return 0
        if s[0] == '+':
            if l == 1:
                return 0
            s = s[1:]
            l -=1
        if s[0] == '-':
            if l == 1:
                return 0
            s = s[1:]
            l -=1
            zheng = 0
        for i in range(l):
            n = ord(s[i])
            if n > 57 or n < 48:
                return 0
            result += (n-48)*10**(l-i-1)
        if zheng == 0:
            return result*(-1)
        return result