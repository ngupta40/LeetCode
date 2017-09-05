def fizzBuzz(n):
    retList = list()
    for i in range(0,n):
        if((i+1)%3 == 0 and (i+1)%15 != 0):
            retList.append("Fizz")
        elif((i+1)%5 == 0 and (i+1)%15 != 0):
            retList.append("Buzz")
        elif((i+1)%15 == 0):
            retList.append("FizzBuzz")
        else:
            retList.append(str(i+1))
    return retList

    """
    :type n: int
    :rtype: List[str]
    """
print fizzBuzz(15)