def arrayPairSum(nums):
    nums.sort()
    minimum = 0
    print nums
    for i in range(0,len(nums),2):
        minimum = minimum + nums[i]

    return minimum

sum = arrayPairSum([7,3,1,0,0,6])

print "Sum",sum