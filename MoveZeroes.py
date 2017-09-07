def moveZeroes(nums):
    n =0
    c = nums.count(0)
    while 0 in nums: nums.remove(0)
    for i in range(0,c):
        nums.append(0)
    print nums
moveZeroes([0, 1, 0, 3, 12])