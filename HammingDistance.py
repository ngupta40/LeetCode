def hammingDistance(x, y):
    binx = bin(x)
    biny = bin(y)
    xlen =  len(binx.split('0b')[1])
    ylen = len(biny.split('0b')[1])
    if(xlen <= ylen):
        padding = abs(ylen-xlen)
    else:
        padding = abs(xlen-ylen)

    paddingString = ''
    for i in range(0,padding):
        paddingString = paddingString + '0'

    if(xlen <= ylen):
        newx = paddingString + binx.split('0b')[1]
        newy = biny.split('0b')[1]
    else:
        newy = paddingString + biny.split('0b')[1]
        newx = binx.split('0b')[1]

    hd =0
    for i in range(0,max(xlen,ylen)):
        if(newy[i] != newx[i]):
           hd = hd +1
    print hd
hammingDistance(100,1000)