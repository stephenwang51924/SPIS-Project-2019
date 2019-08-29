import turtle

def drawGrid():
    # Draws tic tac toe grid.
    t = turtle.Turtle()
    t.hideturtle()
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
    t.write(1, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(40, 55)
    t.pendown()
    t.write(2, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(140, 55)
    t.pendown()
    t.write(3, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(-60, -45)
    t.pendown()
    t.write(4, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(40, -45)
    t.pendown()
    t.write(5, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(140, -45)
    t.pendown()
    t.write(6, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(-60, -145)
    t.pendown()
    t.write(7, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(40, -145)
    t.pendown()
    t.write(8, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(140, -145)
    t.pendown()
    t.write(9, align = "center", font = ("Arial", 10, "normal"))

    t.penup()
    t.setpos(0,0)

# Draws an X in specified box by player1.
def drawX(player1Move):
    t = turtle.Turtle()
    t.speed(0)
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
def drawO(player2Move):
    t = turtle.Turtle()
    t.speed(0)
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
def endGame1(player1List, gameList):
    if "1" in player1List and "2" in player1List and "3" in player1List:
        print("Player1 Wins!")
        return 1
    elif "4" in player1List and "5" in player1List and "6" in player1List:
        print("Player1 Wins!")
        return 1
    elif "7" in player1List and "8" in player1List and "9" in player1List:
        print("Player1 Wins!")
        return 1
    elif "1" in player1List and "4" in player1List and "7" in player1List:
        print("Player1 Wins!")
        return 1
    elif "2" in player1List and "5" in player1List and "8" in player1List:
        print("Player1 Wins!")
        return 1
    elif "3" in player1List and "6" in player1List and "9" in player1List:
        print("Player1 Wins!")
        return 1
    elif "1" in player1List and "5" in player1List and "9" in player1List:
        print("Player1 Wins!")
        return 1
    elif "3" in player1List and "5" in player1List and "7" in player1List:
        print("Player1 Win!")
        return 1
    elif len(gameList) == 9:
        print("Tie Game!")
        return 1

# Checks if player2 has won or if the game is a tie.
def endGame2(player2List, gameList):
    if "1" in player2List and "2" in player2List and "3" in player2List:
        print("Player2 Wins!")
        return 1
    elif "4" in player2List and "5" in player2List and "6" in player2List:
        print("Player2 Wins!")
        return 1
    elif "7" in player2List and "8" in player2List and "9" in player2List:
        print("Player2 Wins!")
        return 1
    elif "1" in player2List and "4" in player2List and "7" in player2List:
        print("Player2 Wins!")
        return 1
    elif "2" in player2List and "5" in player2List and "8" in player2List:
        print("Player2 Wins!")
        return 1
    elif "3" in player2List and "6" in player2List and "9" in player2List:
        print("Player2 Wins!")
        return 1
    elif "1" in player2List and "5" in player2List and "9" in player2List:
        print("Player2 Wins!")
        return 1
    elif "3" in player2List and "5" in player2List and "7" in player2List:
        print("Player2 Win!")
        return 1
    elif len(gameList) == 9:
        print("Tie Game!")
        return 1

# Main function that starts the tic tac toe game.
def playGame():
    drawGrid()
    player1List = []
    player2List = []
    gameList = []
    while True:
        player1Move = input("Enter the number of the box to place the X.")
        drawX(player1Move)
        player1List.append(player1Move)
        gameList.append(player1Move)
        winCon = endGame1(player1List, gameList)
        if winCon == 1:
            break
        player2Move = input("Enter the number of the box to place the O.")
        drawO(player2Move)
        player2List.append(player2Move)
        gameList.append(player2Move)
        winCon = endGame2(player2List, gameList)
        if winCon == 1:
            break


playGame()

