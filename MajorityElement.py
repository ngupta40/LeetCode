def majorityElement(nums):
    numdict = dict()
    if(len(nums)>0):
        for num in nums:
            if(numdict.has_key(num)):
                numdict[num] += 1
            else:
                numdict[num] = 1
        if(max(numdict.values())>((len(nums))/2)):
            return numdict.keys()[numdict.values().index(max(numdict.values()))]
    else:
        return None
    """
    :type nums: List[int]
    :rtype: int
    """
print majorityElement([1,1,2,2,1,1,3,4,5,6,7,1,1,1,1])