def findDisappearedNumbers(nums):
    l1 = list()
    for i in range(0,len(nums)):
        l1.append(i+1)
    return list(set (l1)-set(nums))

print findDisappearedNumbers([])