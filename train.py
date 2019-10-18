import numpy as np
import random

def winCon1(turn):
    if turn[0, 0] == 1 and turn[0, 1] == 1 and turn[0, 2] == 1:
        return True
    elif turn[1, 0] == 1 and turn[1, 1] == 1 and turn[1, 2] == 1:
        return 1
    elif turn[2, 0] == 1 and turn[2, 1] == 1 and turn[2, 2] == 1:
        return True
    elif turn[0, 0] == 1 and turn[1, 0] == 1 and turn[2, 0] == 1:
        return True
    elif turn[0, 1] == 1 and turn[1, 1] == 1 and turn[2, 1] == 1:
        return True
    elif turn[0, 2] == 1 and turn[1, 2] == 1 and turn[2, 2] == 1:
        return True
    elif turn[0, 0] == 1 and turn[1, 1] == 1 and turn[2, 2] == 1:
        return True
    elif turn[2, 0] == 1 and turn[1, 1] == 1 and turn[0, 2] == 1:
        return True
    elif (0 in turn) == False:
        return True
    return False

def winCon2(turn):
    if turn[0, 0] == 2 and turn[0, 1] == 2 and turn[0, 2] == 2:
        return True
    elif turn[1, 0] == 2 and turn[1, 1] == 2 and turn[1, 2] == 2:
        return True
    elif turn[2, 0] == 2 and turn[2, 1] == 2 and turn[2, 2] == 2:
        return True
    elif turn[0, 0] == 2 and turn[1, 0] == 2 and turn[2, 0] == 2:
        return True
    elif turn[0, 1] == 2 and turn[1, 1] == 2 and turn[2, 1] == 2:
        return True
    elif turn[0, 2] == 2 and turn[1, 2] == 2 and turn[2, 2] == 2:
        return True
    elif turn[0, 0] == 2 and turn[1, 1] == 2 and turn[2, 2] == 2:
        return True
    elif turn[2, 0] == 2 and turn[1, 1] == 2 and turn[0, 2] == 2:
        return True
    elif (0 in turn) == False:
        return True
    return False

def winMove(turn):
    for row in range(3):
        for col in range(3):
            if turn[row, col] == 0:
                turn[row, col] = 1
                if winCon1(turn) == True:
                    return True
                else:
                    turn[row, col] = 0
    return False

def blockMove(turn):
    for row in range(3):
        for col in range(3):
            if turn[row, col] == 0:
                turn[row, col] = 2
                if winCon2 == True:
                    turn[row, col] = 1
                    return True
                else:
                    turn[row, col] = 0
    return False


def buildDict(game, dictGame):
    for board in range(len(game) - 1):
            if str(game[board]) not in dictGame:
                dictGame[str(game[board])] = []
                dictGame[str(game[board])].append(game[board + 1])
            else:
                dictGame[str(game[board])].append(game[board + 1])
    return dictGame

def getData():
    while True:
        turn = np.zeros((3, 3))
        game = []
        while True:
            while True:
                if (0 in turn) == False:
                    break
                if winMove(turn) == True:
                    break
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if turn[row, col] == 0:
                    turn[row, col] = 1
                    break
            game.append(np.copy(turn))
            if winCon1(turn) == True:
                break
            while True:
                if (0 in turn) == False:
                    break
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if turn[row, col] == 0:
                    turn[row, col] = 2
                    if winCon2(turn) == True:
                        game.append(np.copy(turn))
                    break
            if winCon1(turn) == True or winCon2(turn) == True:
                break
            if (0 in turn) == False:
                break
        if winCon2(turn) == True:
            return game

if __name__ == "__main__":
    newDict = {}
    print(buildDict(getData(), newDict))

