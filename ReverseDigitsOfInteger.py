import sys
def reverse(x):
    l1 = list()
    flag = 0
    if(x == 0):
        return 0
    if(x < 0):
        flag = 1
        x =0 - x
    while( x > 0):
        mod = x%10
        x= x/10
        l1.append(str(mod))

    l1 =  int(''.join(l1))
    if(flag == 1):
        l1 = 0 - l1
    print "sysMax" , sys.maxint
    if((l1 > sys.maxint) or (l1 < -sys.maxint)):
        return 0
    return l1

l1 = reverse(1534236469)
print l1