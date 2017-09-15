class Solution(object):
    def findRestaurant(self, list1, list2):
        comList = list(set(list1).intersection((set(list2))))
        min = float('inf')
        finalList = list()

        for common in comList:
            if(list1.index(common)+list2.index(common) < min):
                min = list1.index(common)+list2.index(common)
                if(len(finalList)>0): finalList.pop()
                finalList.append(common)
            elif(list1.index(common)+list2.index(common) == min):
                finalList.append(common)

        return finalList

s1 = Solution()
#s1.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"])
s1.findRestaurant(["Shogun", "KFC", "Tapioca Express", "Burger King"],["KFC", "Shogun", "Burger King"])