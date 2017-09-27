class Solution(object):
    def isPowerOfTwo(self, n):
        while(n!=1):
            rem = n%2
            n = n/2
            if(rem%2 == 1):
                return False
        return True
        """
        :type n: int
        :rtype: bool
        """
s1 = Solution()
print s1.isPowerOfTwo(1023)