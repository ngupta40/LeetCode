def matrixReshape(nums, r, c):
    newL = sum(nums,[])
    index = 0
    if( r*c != len(nums) * len(nums[0])):
        return nums
    else:
        rList = list()
        for nr in range(0,r):
            cList = list()
            for nc in range(0,c):
                cList.append(newL[index])
                index = index + 1
            rList.append(cList)

    return rList
print matrixReshape([[1,2,3],[3,4,6]],2,3)