class Solution(object):
    def checkRecord(self, s):
        if(s.count("A") <=1 and s.__contains__("LLL") == False):
            return True
        else:
            return False

        """
        :type s: str
        :rtype: bool
        """
s1 = Solution()
s1.checkRecord("PPAALLP")