class Solution(object):
    def reverseStr(self, s, k):
        list1 = list()
        for i in range(0,len(s),k):
            list1.append(s[i:i+k])
        print list1
        for i in xrange(0,len(list1),2):
            list1[i] = list1[i][::-1]

        return "".join(list1)
s1 = Solution()
print s1.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",39)
print s1.reverseStr("abcdefg",2)