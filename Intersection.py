def intersection(nums1, nums2):
    print nums1,nums2
    snums1 = set(nums1)
    snums2 = set(nums2)
    return list(snums1.intersection(snums2))

i = intersection([1, 2, 2, 1],[2,2])
print i