import train as tr
import numpy as np
import turtle
import random

def drawGrid(t):
    # Draws tic tac toe grid.
    x = turtle.Screen()
    x.bgpic("hi.gif")
    t.hideturtle()
    t.pensize(7)
    t.color("white")
    t.speed(0)
    t.penup()
    t.backward(50)
    t.pendown()
    t.left(90)
    t.forward(150)
    t.backward(300)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.backward(300)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.backward(300)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.backward(300)

    # Numbers each box.
    t.penup()
    t.setpos(-60, 55)
    t.pendown()
    t.pencolor("black")
    t.write(1, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(40, 55)
    t.pendown()
    t.write(2, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(140, 55)
    t.pendown()
    t.write(3, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(-60, -45)
    t.pendown()
    t.write(4, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(40, -45)
    t.pendown()
    t.write(5, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(140, -45)
    t.pendown()
    t.write(6, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(-60, -145)
    t.pendown()
    t.write(7, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(40, -145)
    t.pendown()
    t.write(8, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(140, -145)
    t.pendown()
    t.write(9, align = "center", font = ("Arial", 15, "normal"))

    t.penup()
    t.setpos(0,200)

# Draws an X in specified box by player1.
def drawX(player1Move, t):
    t.speed(0)
    t.pensize(7)
    t.color("red")
    t.hideturtle()

    if player1Move == str(1):
        t.penup()
        t.setpos(-100, 60)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

    if player1Move == str(2):
        t.penup()
        t.setpos(0, 60)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

    if player1Move == str(3):
        t.penup()
        t.setpos(100, 60)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

    if player1Move == str(4):
        t.penup()
        t.setpos(-100, -40)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

    if player1Move == str(5):
        t.penup()
        t.setpos(0, -40)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

    if player1Move == str(6):
        t.penup()
        t.setpos(100, -40)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

    if player1Move == str(7):
        t.penup()
        t.setpos(-100, -140)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

    if player1Move == str(8):
        t.penup()
        t.setpos(0, -140)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

    if player1Move == str(9):
        t.penup()
        t.setpos(100, -140)
        t.pendown()
        t.write("X", align = "center", font = ("Arial", 50, "normal"))

# Draws an O in specified box by player2.
def drawO(player2Move, t):
    t.speed(0)
    t.pensize(7)
    t.color("blue")
    t.hideturtle()

    if player2Move == str(1):
        t.penup()
        t.setpos(-100, 60)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

    if player2Move == str(2):
        t.penup()
        t.setpos(0, 60)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

    if player2Move == str(3):
        t.penup()
        t.setpos(100, 60)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

    if player2Move == str(4):
        t.penup()
        t.setpos(-100, -40)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

    if player2Move == str(5):
        t.penup()
        t.setpos(0, -40)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

    if player2Move == str(6):
        t.penup()
        t.setpos(100, -40)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

    if player2Move == str(7):
        t.penup()
        t.setpos(-100, -140)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

    if player2Move == str(8):
        t.penup()
        t.setpos(0, -140)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

    if player2Move == str(9):
        t.penup()
        t.setpos(100, -140)
        t.pendown()
        t.write("O", align = "center", font = ("Arial", 50, "normal"))

# Checks if player1 has won or if the game is a tie.
def endGame1(player1List, gameList, t):
    if "1" in player1List and "2" in player1List and "3" in player1List:
        t.speed(0)
        t.penup()
        t.setpos(-145,100)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Player1 Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "4" in player1List and "5" in player1List and "6" in player1List:
        t.speed(0)
        t.penup()
        t.setpos(-145,0)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Player1 Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "7" in player1List and "8" in player1List and "9" in player1List:
        t.speed(0)
        t.penup()
        t.setpos(-145,-100)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Player1 Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "1" in player1List and "4" in player1List and "7" in player1List:
        t.speed(0)
        t.penup()
        t.setpos(-100,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(90)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Player1 Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "2" in player1List and "5" in player1List and "8" in player1List:
        t.speed(0)
        t.penup()
        t.setpos(0,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(90)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Player1 Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "3" in player1List and "6" in player1List and "9" in player1List:
        t.speed(0)
        t.penup()
        t.setpos(100,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(90)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Player1 Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "1" in player1List and "5" in player1List and "9" in player1List:
        t.speed(0)
        t.penup()
        t.setpos(-145,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(45)
        t.forward(400)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Player1 Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "3" in player1List and "5" in player1List and "7" in player1List:
        t.speed(0)
        t.penup()
        t.setpos(145,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(135)
        t.forward(400)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Player1 Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif len(gameList) == 9:
        t.speed(0)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Tie Game!", align = "center", font = ("Arial", 50, "bold"))
        return 1
    return 0

# Checks if player2 has won or if the game is a tie.
def endGame2(player2List, gameList, t):
    if "1" in player2List and "2" in player2List and "3" in player2List:
        t.speed(0)
        t.penup()
        t.setpos(-145,100)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Computer Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "4" in player2List and "5" in player2List and "6" in player2List:
        t.speed(0)
        t.penup()
        t.setpos(-145,0)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Computer Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "7" in player2List and "8" in player2List and "9" in player2List:
        t.speed(0)
        t.penup()
        t.setpos(-145,-100)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Computer Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "1" in player2List and "4" in player2List and "7" in player2List:
        t.speed(0)
        t.penup()
        t.setpos(-100,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(90)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Computer Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "2" in player2List and "5" in player2List and "8" in player2List:
        t.speed(0)
        t.penup()
        t.setpos(0,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(90)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Computer Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "3" in player2List and "6" in player2List and "9" in player2List:
        t.speed(0)
        t.penup()
        t.setpos(100,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(90)
        t.forward(290)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Computer Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "1" in player2List and "5" in player2List and "9" in player2List:
        t.speed(0)
        t.penup()
        t.setpos(-145,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(45)
        t.forward(400)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Computer Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif "3" in player2List and "5" in player2List and "7" in player2List:
        t.speed(0)
        t.penup()
        t.setpos(145,145)
        t.pendown()
        t.pencolor("black")
        t.pensize(10)
        t.right(135)
        t.forward(400)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Computer Wins!", align = "center", font = ("Arial", 50, "bold"))
        return 1

    elif len(gameList) == 9:
        t.speed(0)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Tie Game!", align = "center", font = ("Arial", 50, "bold"))
        return 1
    return 0

def checkBotWin(player2List, gameList):
    if "1" in player2List and "2" in player2List and "3" in player2List:
        return 1
    elif "4" in player2List and "5" in player2List and "6" in player2List:
        return 1
    elif "7" in player2List and "8" in player2List and "9" in player2List:
        return 1
    elif "1" in player2List and "4" in player2List and "7" in player2List:
        return 1
    elif "2" in player2List and "5" in player2List and "8" in player2List:
        return 1
    elif "3" in player2List and "6" in player2List and "9" in player2List:
        return 1
    elif "1" in player2List and "5" in player2List and "9" in player2List:
        return 1
    elif "3" in player2List and "5" in player2List and "7" in player2List:
        return 1
    elif len(gameList) == 9:
        return 1
    return 0

def mToAx(p1M):
    if p1M == str(1):
        return 0
    elif p1M == str(2):
        return 0
    elif p1M == str(3):
        return 0
    elif p1M == str(4):
        return 1
    elif p1M == str(5):
        return 1
    elif p1M == str(6):
        return 1
    elif p1M == str(7):
        return 2
    elif p1M == str(8):
        return 2
    elif p1M == str(9):
        return 2

def mToAy(p1M):
    if p1M == str(1):
        return 0
    elif p1M == str(2):
        return 1
    elif p1M == str(3):
        return 2
    elif p1M == str(4):
        return 0
    elif p1M == str(5):
        return 1
    elif p1M == str(6):
        return 2
    elif p1M == str(7):
        return 0
    elif p1M == str(8):
        return 1
    elif p1M == str(9):
        return 2

def aToM(row, col):
    if (row, col) == (0, 0):
        return 1
    elif (row, col) == (0, 1):
        return 2
    elif (row, col) == (0, 2):
        return 3
    elif (row, col) == (1, 0):
        return 4
    elif (row, col) == (1, 1):
        return 5
    elif (row, col) == (1, 2):
        return 6
    elif (row, col) == (2, 0):
        return 7
    elif (row, col) == (2, 1):
        return 8
    elif (row, col) == (2, 2):
        return 9

def trainBot():
    dictGame = {}
    for number in range(100000):
        data = tr.getData()
        dictGame = tr.buildDict(data, dictGame)
        if number % 1000 == 0:
            print(number)
    return dictGame

def playBot(dictionary):
    dictGame = dictionary
    loseDict = {}
    t = turtle.Turtle()
    play = "YES"
    while True:
        t.reset()
        drawGrid(t)
        player1List = []
        player2List = []
        gameList = []
        turn = []
        board = np.zeros((3, 3))
        while True:
            player1Move = input("Enter the number of the box to place the X.")
            while not (player1Move == str(1) or player1Move == str(2) or player1Move == str(3) or player1Move == str(4) or player1Move == str(5) or player1Move == str(6) or player1Move == str(7) or player1Move == str(8) or player1Move == str(9)):
                player1Move = input("Enter the number of the box to place the X.")
            repeatMove = True
            while repeatMove == True:
                if player1Move in gameList:
                    print("That spot is already taken!")
                    player1Move = input("Enter the number of the box to place the X.")
                else:
                    repeatMove = False
            x = mToAx(player1Move)
            y = mToAy(player1Move)
            board[x, y] = 1
            drawX(player1Move, t)
            player1List.append(player1Move)
            gameList.append(player1Move)
            turn.append(np.copy(board))
            winCon = endGame1(player1List, gameList, t)
            if winCon == 1:
                break
            
            if str(board) in dictGame:
                while True:
                    nextMove = random.choice(dictGame[str(board)])
                    if str(nextMove) not in loseDict:
                        break
                for row in range(3):
                    for col in range(3):
                        if board[row, col] == 0 and nextMove[row, col] == 2:
                            board[row, col] = 2
                            botMove = str(aToM(row, col))
                            drawO(botMove, t)
                            player2List.append(botMove)
                            gameList.append(botMove)
                            winCon = endGame2(player2List, gameList, t)
                            if winCon == 1:
                                turn.append(np.copy(board))
            else:
                while True:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if board[row, col] == 0:
                        board[row, col] = 2
                        botMove = str(aToM(row, col))
                        drawO(botMove, t)
                        player2List.append(botMove)
                        gameList.append(botMove)
                        winCon = endGame2(player2List, gameList, t)
                        if winCon == 1:
                            turn.append(np.copy(board))
                        break
            if winCon == 1:
                    break
        if checkBotWin(player2List, gameList) == 0:
            tr.buildDict(turn, loseDict)
            print(loseDict)
        if checkBotWin(player2List, gameList) == 1:
            tr.buildDict(turn, dictGame)
            print(dictGame)
        play = input("Type YES if you want to play again and NO if you want to quit.").upper()
        while not (play == "YES" or play == "NO"):
            play = input("Type YES if you want to play again and NO if you want to quit.").upper()

playBot(trainBot())
