# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    l = ''
    def FirstAppearingOnce(self):
        # write code here
        for s in self.l:
            if self.l.count(s) == 1:
                return s
        return '#'
    def Insert(self, char):
        # write code here
        self.l = self.l + char