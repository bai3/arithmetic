# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        p = [pRoot]
        a = 0
        while p:
            tmp = []
            buf = []
            for i in p:
                buf.append(i.val)
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            if a%2 == 1:
                buf.reverse()
            res.append(buf)
            p = tmp
            a+=1
        return res