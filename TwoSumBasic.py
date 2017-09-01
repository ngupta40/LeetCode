def twoSum(self, nums, target):
    length = len(nums)
    for i in range(0, length):
        l1 = list();
        rem = 0;
        l1.append(i)
        rem = target - nums[i]
        for j in range(i + 1, length):
            if (nums[j] == rem):
                l1.append(j)
                return l1

nums = [1,2,3,4,5,9]

l1 = twoSum(nums,9)
print l1