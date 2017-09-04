def distributeCandies(candies):
    newList = set(candies)
    return min(len(candies)/2,len(newList))

print distributeCandies([1,1,2,2,3,3,4,4,5,6])