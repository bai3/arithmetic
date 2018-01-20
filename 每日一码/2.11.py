# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        a = [pRoot]
        d = 0
        while a:
            b = []
            for i in a:
                if i.left:
                    b.append(i.left)
                if i.right:
                    b.append(i.right)
            a = b
            d +=1
        return d