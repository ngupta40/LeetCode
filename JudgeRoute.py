def judgeCircle(moves):
    totalmoves = len(moves)
    MoveList = list()
    print totalmoves
    if(totalmoves % 2 != 0):
        return False
    else:
        for i in range(0,totalmoves):
            MoveList.append(moves[i])
        if((MoveList.count('L')- MoveList.count('R') == 0) and (MoveList.count('U') - MoveList.count('D') == 0)):
            return True

moves = "LRUDLRUDLLLRRR"
judegement = judgeCircle(moves)
print judegement