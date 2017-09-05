def findMaxConsecutiveOnes(nums):
    retVal = 0
    sVal = 0
    for i in range(0,len(nums)):
        if(nums[i] == 1):
            sVal = sVal + 1
            if(i == len(nums)-1 and sVal > retVal):
                retVal = sVal
        else:
            if sVal > retVal:
                retVal = sVal
            sVal = 0
    return retVal

print findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,1,0,1,1,1,1,1,1])