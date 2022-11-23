from tkinter import CENTER
import turtle
import random
import time

#Full path: r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\

# create levels
levels = []
levelLayout = [
    "XXXXXXXXXXXXXXXXXXXXX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XX",
    "XXXXXXXXXXXXXXXXXXXXX",]

level1 = [
    "XXXXXXXXXXXXXXXXXXXXX",
    "XP          C   X   X",
    "XXYXXXXXXXXXXXX X X X",
    "X    C  X   X   X X X",
    "X XXXXX X X X XXX X X",
    "X X   X X X   X   X X",
    "X X X X XCXXXXX XXX X",
    "X X XOX X     X X X X",
    "X X XXX XXXXX X X X X",
    "X X   X   X   XCX   X",
    "X X X XXX X XXX XXXXX",
    "X X Y   X Y X       X",
    "X XCX XXX X XXXXX X X",
    "X X X     X  C  X X X",
    "X XXXXXXX XXXXX XXX X",
    "X X     X     X     X",
    "X X XXX XXXXX XXXXX X",
    "X   X X  C  X     XCX",
    "X XXX XXXXX XXXXXXX X",
    "X    C    X         X",
    "XXXXXXXXXXXXXXXXXXXXX",]
levels.append(level1)

level2 = [
    "XXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXP      XXXXXXX",
    "XXXXXXX X XXX XXXXXXX",
    "XXXXX XCX X X   XXXXX",
    "XXXXX XXX X XXX XXXXX",
    "XXX X X   X   X X XXX",
    "XXX X X XXXCX X X XXX",
    "XXX X X X X X   C XXX",
    "XXX X XCX X XXXYXXXXX",
    "X   X   X   X     XOX",
    "X X XXXXX XXX XXX X X",
    "X X  C    X   X X   X",
    "XXX XXXXXXX X X XXXXX",
    "XXX X     C X   C XXX",
    "XXX XXX X XXX XXX XXX",
    "XXX  CX X X X X   XXX",
    "XXXXX XXX X XXX XXXXX",
    "XXXXX   X  CX   XXXXX",
    "XXXXXXX XXXXX XXXXXXX",
    "XXXXXXX  C    XXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXX",]
levels.append(level2)

level3 = [
    "XXXXXXXXXXXXXXXXXXXXX",
    "X   C        PX     X",
    "X X XXX XXXXXXX X X X",
    "X X X   X  C    XCX X",
    "X X XXXXX XXXYXXX X X",
    "X X     X   X   X XOX",
    "XXXXXXX XXX X XXX XXX",
    "X   C     X X   X   X",
    "X X XXXXXXX X X XXX X",
    "X X X     C X X X   X",
    "X XXX XXXXXXXXX X X X",
    "X   X           X X X",
    "X X XXX XXXYXXXXX X X",
    "XCX  CX X   C   X X X",
    "XXX X X X XXXXX XCX X",
    "X   X X X X   X X   X",
    "X XXXXX X X XXX XXX X",
    "X   C   X X X C X  CX",
    "X XXXXXXX X X XXX X X",
    "X   X    CX    C  X X",
    "XXXXXXXXXXXXXXXXXXXXX",]
levels.append(level3)

level4 = [
    "XXXXXXXXXXXXXXXXXXXXX",
    "XP    X   X     C   X",
    "XXXXX XXX X X XXXXX X",
    "X   X   X   X X X   X",
    "XXX XYX XXXXX X X XXX",
    "X   X X  C    X X  CX",
    "X X X XXXXXXXXX XXX X",
    "X X   X       X C X X",
    "X XXX XXX XXX X X X X",
    "X X X C X X C X X X X",
    "X X XXX X X XXX X X X",
    "XCX   X X X   X XCX X",
    "X X X X X XXX X X X X",
    "X X XOX  CX X X X X X",
    "X X XXXXXXX X X Y X X",
    "X X          C  X XCX",
    "X XXXXXXX XXXXXXXXX X",
    "X  C    X   X C X   X",
    "X XXXXX XXXXX X X XXX",
    "X     X   C   X     X",
    "XXXXXXXXXXXXXXXXXXXXX",]
levels.append(level4)

level5 = [
    "XXXXXXXXXXXXXXXXXXXXX",
    "X     C             X",
    "XXX XXX XXXXX X XXXXX",
    "X     XPX     X  C  X",
    "X XXXXXXX XXX XXXXX X",
    "X     X     X    CX X",
    "XYXXX XXXXX X XXX X X",
    "X X   C   X X X   X X",
    "X XXXXX X X XXX XXX X",
    "X   X   X XCX   X C X",
    "X X XXX XXXXXXXXX X X",
    "X X X   X         X X",
    "XCXXXXXYXXX X XXXXX X",
    "X   X   X   X   X  CX",
    "X XXX XXX X XXXXX XXX",
    "X X C X   X X       X",
    "XXX X X X XXXXX XXXXX",
    "X   X   X X  C      X",
    "X X X X XXXXXXX XXX X",
    "X XOX X  C  X     X X",
    "XXXXXXXXXXXXXXXXXXXXX",]
levels.append(level5)

level6 = [
    "XXXXXXXXXXXXXXXXXXXXX",
    "YYPYYYYYYYYYYYYYYYXXX",
    "YXXXXXXXXX XXXXXXXXXX",
    "YXXXXXXXXXYXXXXXXXXXX",
    "YXXXXXXXXXYXXXXXXXXXX",
    "YXXXXXXXXXYYYY  XXXXX",
    "YXXXXXXXXXXXXXXYXXXXX",
    "YXXXXXXXXXXXXXXYXXXXX",
    "YXXXXXXXXXXXXXXYXXXXX",
    "YXXXXXXXXXXXXXXYXXXXX",
    "YXXYYYYYYYYXXXXYXXXXX",
    "YXXYXXXXXYYYYYY XXXXX",
    "YXXYXXXXXXYXXXXYXXXXX",
    "YXXYXXXXXXYYYYYYXXXXX",
    "YXXYXXXXXXXXXXXXXXXXX",
    "YXXYXXXXXXXXXXXXXXXXX",
    "YXXYXXXXXXXXXXXXXXXXX",
    "YXXYYYYYYYYYYYYYXXXXX",
    "YXXXXXXXXXXXXXXYYYYXX",
    "YXXXXXXXXXXXXXXXXXOXX",
    "YYYYYYYYYYYYYYYYYYYXX",]
levels.append(level6)

def Main(levels):
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Exit_Icon.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\NextLevel_Icon.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Objective.gif",shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Player.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Player2.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Player3.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Player4.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Wall.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Level_BG.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Coin.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Claimed_Coin.gif", shape=None)

    walls = []
    player_cord = []
    Next_level_cord = []
    Wallet = []
    location = 0, 0
    Score = 0
    stage = 0
    
    for r in range(len(levels[stage])):
        wn = turtle.Screen()
        wn.title("Maze")
        wn.bgcolor('Black')
        wn.setup(700, 700)
        wn.tracer(0)

        player = turtle.Turtle()
        player.speed(0)
        Icon = random.randint(1,4)
        if Icon == 1:
            player.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Player.gif")
        elif Icon == 2:
            player.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Player2.gif")
        elif Icon == 3:
            player.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Player3.gif")
        elif Icon == 4:
            player.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Player4.gif")
        player.color("red")
        player.penup()

        tile = turtle.Turtle()
        tile.color("white")
        tile.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Wall.gif")
        tile.speed(0)
        tile.penup()

        Invisibletile = turtle.Turtle()
        Invisibletile.color("white")
        Invisibletile.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Wall.gif")
        Invisibletile.speed(0)
        Invisibletile.penup()

        Coin = turtle.Turtle()
        Coin.color("white")
        Coin.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Coin.gif")
        Coin.speed(0)
        Coin.penup()

        ClaimedCoin = turtle.Turtle()
        ClaimedCoin.color("white")
        ClaimedCoin.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Claimed_Coin.gif")
        ClaimedCoin.speed(0)
        ClaimedCoin.penup()

        objective = turtle.Turtle()
        objective.speed(0)
        objective.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Objective.gif")
        objective.color("yellow")
        objective.penup()

        ExitButton = turtle.Turtle()
        ExitButton.penup()
        ExitButton.speed(0)
        ExitButton.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Exit_Icon.gif")
        ExitButton.pencolor("white")
        ExitButton.setx(35)
        ExitButton.sety(-275)
        ExitButton.shapesize(1.5, 3)
        ExitButton.goto(35, -275)

        NextLevelButton = turtle.Turtle()
        NextLevelButton.penup()
        NextLevelButton.speed(0)
        NextLevelButton.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\NextLevel_Icon.gif")
        NextLevelButton.pencolor("white")
        NextLevelButton.setx(-35)
        NextLevelButton.sety(-275)
        NextLevelButton.shapesize(1.5, 3)
        NextLevelButton.goto(-35, -275)

        pen = turtle.Turtle()
        pen.penup()
        pen.hideturtle()
        pen.speed(0)
        pen.color("blue")

        scorepen = turtle.Turtle()
        scorepen.penup()
        scorepen.hideturtle()
        scorepen.speed(0)
        scorepen.color("blue")
        scorepen.goto(125, 265)
        scorepen.write("Score: "+str(Score), align="center", font=("Courier", 24, "bold"))

        LevelInd = turtle.Turtle()
        LevelInd.penup()
        LevelInd.hideturtle()
        LevelInd.speed(0)
        LevelInd.color("blue")
        LevelInd.goto(-125, 265)

        for y in range(len(levels[r])):
            for x in range(len(levels[r][y])):
                location = levels[r][y][x]
                screen_x = -240 + (x * 24)
                screen_y = 240 - (y * 24)

                if location == 'X':
                    tile.goto(screen_x,screen_y)
                    tile.stamp()
                    walls.append((screen_x, screen_y))
                elif location == 'Y':
                    Invisibletile.goto(screen_x,screen_y)
                    Invisibletile.stamp()
                elif location == 'C':
                    Coin.goto(screen_x,screen_y)
                    Coin.stamp()
                    Wallet.append((screen_x, screen_y))
                elif location == 'P':
                    player.goto(screen_x,screen_y)
                    player_cord.append((screen_x,screen_y))
                elif location == 'O':
                    objective.goto(screen_x,screen_y)
                    objective.stamp()
                    Next_level_cord.append((screen_x,screen_y))

        Loop = True
        while Loop:

            def ClickButtons(x,y):
                if (x > 5 and x < 65) and (y < -260 and y > -390):
                    wn.bye()

                if (x < -5 and x > -65) and (y < -260 and y > -390):
                    player.goto(Next_level_cord[0])               

            def KeyQuit():
                wn.bye()

            def KeySkip():
                player.goto(Next_level_cord[0])

            def player_up():
                if player.ycor() < 225 and ((player.xcor(), player.ycor() + 24) not in walls):
                    y = player.ycor()
                    y += 24
                    player.sety(y)

            def player_down():
                if player.ycor() > -225 and ((player.xcor(), player.ycor() - 24) not in walls):
                    y = player.ycor()
                    y -= 24
                    player.sety(y)

            def player_right():
                if player.xcor() < 225 and ((player.xcor() + 24, player.ycor()) not in walls):
                    x = player.xcor()
                    x += 24
                    player.setx(x)

            def player_left():
                if player.xcor() > -225 and ((player.xcor() - 24, player.ycor()) not in walls):
                    x = player.xcor()
                    x -= 24
                    player.setx(x)

            LevelInd.clear()
            LevelInd.write("Level: "+str(stage+1),  align="center", font=("Courier", 24, "bold"))

            player_current = (player.xcor(), player.ycor())

            if player_current in Next_level_cord:
                walls.clear()
                player_cord.clear()
                Next_level_cord.clear()
                Wallet.clear()
                scorepen.clear()
                LevelInd.clear()
                wn.clear()

                tile.clearstamps()
                Invisibletile.clearstamps()
                player.clearstamps()
                objective.clearstamps()
                Coin.clearstamps()
                ClaimedCoin.clearstamps()

                wn = turtle.Screen()
                wn.title("Maze")
                wn.bgcolor('Black')
                wn.setup(700, 700)
                wn.tracer(0)

                border = turtle.Turtle()
                border.color("white")
                border.speed(0)
                border.penup()
                border.hideturtle()
                border.goto(250,250)
                border.pendown()
                border.goto(250,-250)
                border.goto(-250,-250)
                border.goto(-250,250)
                border.goto(250,250)

                Loop = False
                stage += 1

                for q in range(2):
                    if stage >= len(levels):
                        for p in range(5):
                            wn.update()
                            wn.bgpic(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Level_BG.gif")
                            pen.write("YOU WIN!!", align=CENTER, font=("Verdana", 50, "normal"))
                        wn.bye()
                    else:
                        wn.update()
                        wn.bgpic(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Level_BG.gif")
                        pen.write("Next level", align=CENTER, font=("Verdana", 60, "normal"))
                        time.sleep(0.75)
                    
                pen.clear()
                border.clear()
                wn.clear()
                
            if player_current in Wallet:
                Wallet.remove(player_current)
                ClaimedCoin.goto(player_current)
                ClaimedCoin.stamp()
                Score += 1
                
                scorepen.clear()
                scorepen.write("Score: "+str(Score), align="center", font=("Courier", 24, "bold"))

            #Keyboard binding
            wn.listen()
            wn.onkeypress(player_up, "w")
            wn.onkeypress(player_down, "s")
            wn.onkeypress(player_left, "a")
            wn.onkeypress(player_right, "d")
            wn.onkeypress(KeySkip, "n")
            wn.onkeypress(KeyQuit, 'Escape')

            wn.update()
            wn.bgpic(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Level_BG.gif")
            wn.onclick(ClickButtons)

def StartUp():
    wn = turtle.Screen()
    wn.title("Maze")
    wn.bgcolor('Black')
    wn.setup(700, 700)
    wn.tracer(0)

    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Start_Icon.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Exit_Icon.gif", shape=None)
    turtle.addshape(name=r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Menu_BG.gif", shape=None)

    border = turtle.Turtle()
    border.color("white")
    turtle.speed(0)
    border.penup()
    border.hideturtle()
    border.goto(250,250)
    border.pendown()
    border.goto(250,-250)
    border.goto(-250,-250)
    border.goto(-250,250)
    border.goto(250,250)

    StartButton = turtle.Turtle()
    StartButton.penup()
    StartButton.speed(0)
    StartButton.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Start_Icon.gif")
    StartButton.pencolor("white")
    StartButton.shapesize(1.5, 3)
    StartButton.goto(0,25)

    ExitButton = turtle.Turtle()
    ExitButton.penup()
    ExitButton.speed(0)
    ExitButton.shape(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Exit_Icon.gif")
    ExitButton.pencolor("white")
    ExitButton.setx(0)
    ExitButton.sety(-25)
    ExitButton.shapesize(1.5, 3)
    ExitButton.goto(0, -25)

    def ClickButtons(x,y):
        if (x > -30 and x < 30) and (y < 40 and y > 10):
            wn.clear()
            StartButton.clear()
            StartButton.hideturtle()
            border.clear()

            Main(levels)

        if (x > -30 and x < 30) and (y < -5 and y > -55):
            wn.bye()
    
    def KeyStart():
        wn.clear()
        StartButton.clear()
        StartButton.hideturtle()
        border.clear()
        Main(levels)
    
    while True:
        wn.update()
        wn.bgpic(r"C:\\Users\\Aldrich Fernandes\\Python\\Scripts\\Projects\\Maze\\Assets\\Menu_BG.gif")
        wn.onclick(ClickButtons)

        wn.listen()
        wn.onkeypress(KeyStart, 'Return')

def Rules():
    wn = turtle.Screen()
    wn.title("Maze")
    wn.bgcolor('Black')
    wn.setup(700, 700)
    wn.tracer(0)

    border = turtle.Turtle()
    border.color("white")
    turtle.speed(0)
    border.penup()
    border.hideturtle()
    border.goto(250,250)
    border.pendown()
    border.goto(250,-250)
    border.goto(-250,-250)
    border.goto(-250,250)
    border.goto(250,250)

    for m in range(25):
        wn.update()

        Rule = turtle.Turtle()
        Rule.penup()
        Rule.hideturtle()
        Rule.speed(0)
        Rule.color("Blue")
        Rule.goto(0,-200)

        Rule.write("WELCOME!!\n'W' = UP\n'S' = DOWN\n'A' = LEFT\n'D' = RIGHT\n'n' = SKIP",align="center", font=("Courier", 48, "bold"))

    Rule.clear()
    border.clear()
    wn.clear()
    StartUp()
        

Rules()