class Solution(object):
    def isAnagram(self, s, t):
        charDict = dict()
        if(len(s) == len(t) and len(s) == 0):
            return True
        if(len(s) == len(t)):
            for chars in s:
                if(charDict.has_key(chars)):
                    charDict[chars] += 1
                else:
                    charDict[chars] = 1
            for char in t:
                if(charDict.has_key(char)):
                    charDict[char] -= 1
                else:
                    return False

            if(max(charDict.values()) == 0):
                return True
            else:
                return False
        else:
            return False

s1 = Solution()
print s1.isAnagram("anagram","nargaam")