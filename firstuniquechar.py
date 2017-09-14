def firstUniqChar(s):
    allChars = "abcdefghijklmnopqrstuvwxyz"
    index = list()
    for chars in allChars:
        if(s.count(chars) == 1):
            index.append(s.index(chars))
    if len(index)> 0:
        return min(index)
    else:
        return -1



print firstUniqChar("loveleetcode")
#"aadadaad"
#"dddccdbba"
#loveleetcode
