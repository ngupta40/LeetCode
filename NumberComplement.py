def findComplement(num):
    bNum = bin(num)
    sbNum = bNum.split('0b')[1]
    cList = list()

    for i in range(0,len(sbNum)):
        if(sbNum[i] == '0'):
            cList.append('1')
        if(sbNum[i] == '1'):
            cList.append('0')

    conv = "".join(cList)
    return int(conv,2)

val = findComplement(10)
print val