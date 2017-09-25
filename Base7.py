class Solution(object):
    def convertToBase7(self, num):
        flagNeg = 0
        if(num < 0):
            flagNeg = 1
        num = abs(num)
        s1 = ""
        while num >= 7:
            base7 = num % 7
            num /= 7
            s1 = str(base7) + s1
        s1 = str(num) + s1
        if(flagNeg == 1):
            s1 = "-" + s1

        return s1
s1 = Solution()
print s1.convertToBase7(0)