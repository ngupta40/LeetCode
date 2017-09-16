class Solution(object):
    def containsDuplicate(self, nums):
        numDict = dict()
        for integer in nums:
            if(numDict.has_key(integer)):
                return True
            else:
                numDict[integer] = 1
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
s1 = Solution()
print s1.containsDuplicate([1,5,-2,-4,0])