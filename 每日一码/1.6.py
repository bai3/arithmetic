class Solution:
    def rectCover(self, number):
        # write code here
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
            print(c)
            return c
obj = Solution()
obj.rectCover(number=4)
