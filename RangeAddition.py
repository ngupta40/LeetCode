def maxCount(m, n, ops):
    minXVal = m
    minYVal = n
    for op in ops:
        minXVal = min(minXVal,op[0])
        minYVal = min(minYVal,op[1])
    return minXVal*minYVal

countMaxval = maxCount(39999,39999,[[19999,19999]])
print countMaxval