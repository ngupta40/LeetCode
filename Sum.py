def getSum(a, b):
    sa = set()
    sa.add(a)
    sa.add(b)
    return sum(sa)
print getSum(2,3)