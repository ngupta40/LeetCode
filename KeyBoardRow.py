def findWords(words):
    dictKBRow = {1:['q','w','e','r','t','y','u','i','o','p'],2:['a','s','d','f','g','h','j','k','l'],3:['z','x','c','v','b','n','m']}
    retList = list()
    newWords = list()

    for i in range(0,len(words)):
        newWords.append(words[i].lower())

    index = - 1
    for word in newWords:
        index  = index + 1
        if dictKBRow.values()[0].__contains__(word[0]):
            flag = 0
            for char in word:
                if dictKBRow.values()[0].__contains__(char):
                    flag = 1
                else:
                    flag = 0
                    break
            if flag ==1:
                retList.append(words[index])
        elif dictKBRow.values()[1].__contains__(word[0]):
            flag = 0
            for char in word:
                if dictKBRow.values()[1].__contains__(char):
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                retList.append(words[index])
        else:
            for char in word:
                flag = 0
                if dictKBRow.values()[2].__contains__(char):
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                retList.append(words[index])
    return retList

finalWords = findWords(["a","b"])
print finalWords