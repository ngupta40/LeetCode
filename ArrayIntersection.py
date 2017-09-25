class Solution(object):
    def intersect(self, nums1, nums2):
        dict1 =dict()
        print nums1,nums2
        for num1 in nums1:
            if(dict1.has_key(num1)):
                dict1[num1] += 1
            else:
                dict1[num1] = 1

        print dict1
        jList = list()
        for num2 in nums2:
            if(dict1.has_key(num2) and dict1[num2] != 0):
                dict1[num2] -= 1
                jList.append(num2)

        print jList
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

s1 = Solution()
s1.intersect([1, 2, 2, 1],[2,2])