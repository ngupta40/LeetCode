def singleNumber(nums):
    dict1 = dict()

    for i in range(0,len(nums)):
        if dict1.has_key(nums[i]):
            dict1[nums[i]] = dict1[nums[i]] + 1
        else:
            dict1[nums[i]] = 1

    return dict1.keys()[dict1.values().index(1)]

singleNumber([6,6,2,2,3,4,4,5,5])