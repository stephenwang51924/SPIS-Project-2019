import turtle

def drawGrid(t):
    # Draws tic tac toe grid.
    x = turtle.Screen()
    turtle.screensize(1200,676)
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
        input()
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
        input()
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
        input()
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
        input()
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
        input()
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
        input()
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
        input()
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
        input()
        return 1

    elif len(gameList) == 9:
        t.speed(0)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Tie Game!", align = "center", font = ("Arial", 50, "bold"))
        input()
        return 1

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
        t.write("Player2 Wins!", align = "center", font = ("Arial", 50, "bold"))
        input()
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
        t.write("Player2 Wins!", align = "center", font = ("Arial", 50, "bold"))
        input()
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
        t.write("Player2 Wins!", align = "center", font = ("Arial", 50, "bold"))
        input()
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
        t.write("Player2 Wins!", align = "center", font = ("Arial", 50, "bold"))
        input()
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
        t.write("Player2 Wins!", align = "center", font = ("Arial", 50, "bold"))
        input()
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
        t.write("Player2 Wins!", align = "center", font = ("Arial", 50, "bold"))
        input()
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
        t.write("Player2 Wins!", align = "center", font = ("Arial", 50, "bold"))
        input()
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
        t.write("Player2 Wins!", align = "center", font = ("Arial", 50, "bold"))
        input()
        return 1

    elif len(gameList) == 9:
        t.speed(0)
        t.penup()
        t.setpos(0,200)
        t.pencolor("black")
        t.hideturtle()
        t.write("Tie Game!", align = "center", font = ("Arial", 50, "bold"))
        input()
        return 1

# Main function that starts the tic tac toe game.
def playGame():
    t = turtle.Turtle()
    play = "YES"
    while play == "YES":
        t.reset()
        drawGrid(t)
        player1List = []
        player2List = []
        gameList = []
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
            drawX(player1Move, t)
            player1List.append(player1Move)
            gameList.append(player1Move)
            winCon = endGame1(player1List, gameList, t)
            if winCon == 1:
                break

            player2Move = input("Enter the number of the box to place the O.")
            while not (player2Move == str(1) or player2Move == str(2) or player2Move == str(3) or player2Move == str(4) or player2Move == str(5) or player2Move == str(6) or player2Move == str(7) or player2Move == str(8) or player2Move == str(9)):
                player2Move = input("Enter the number of the box to place the O.")
            repeatMove = True
            while repeatMove == True:
                if player2Move in gameList:
                    print("That spot is already taken!")
                    player2Move = input("Enter the number of the box to place the O.")
                else:
                    repeatMove = False
            drawO(player2Move, t)
            player2List.append(player2Move)
            gameList.append(player2Move)
            winCon = endGame2(player2List, gameList, t)
            if winCon == 1:
                break
        play = input("Type YES if you want to play again and NO if you want to quit.").upper()
        while not (play == "YES" or play == "NO"):
            play = input("Type YES if you want to play again and NO if you want to quit.").upper()


if __name__ == "__main__":
    playGame()
