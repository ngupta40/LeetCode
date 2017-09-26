class Solution(object):
    def missingNumber(self, nums):
        endTerm = len(nums)
        return (endTerm * (endTerm +1))/2 - sum(nums)




s1 = Solution()
print s1.missingNumber([0,1,3,4])