import math
import random
import turtle
#import time

win_length = 500
win_height = 500

turtles = 8

turtle.screensize(win_length, win_height)


class racer(object):
    def _int_(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turtle.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

        def move(self):
            r = random.randrange(1, 20)
            self.pos = (self.pos[0], self.pos[1] + r)
            self.turt.pendown()
            self.turt.forward(r)

        def reset(self):
            self.turt.penup()
            self.turt.setpos(self.pos)


def setupFile(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + ' 0\n')
    file.close()


def startGame():
    tList = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = [
        "red", "green", "blue", 'yellow', 'pink', 'orange', 'pruple', 'black',
        'grey'
    ]
    start = -(win_length / 2) + 20
    for t in range(turtles):
        newPosX = start + t * (win_length) // turtles
        tList.append(racer(colors[t], (newPosX, -230)))
        tList[t].turt.showturtle()

        run = True
        while run:
            for t in tList:
                t.move()

            maxColor = []
            maxDis = 0
            for t in tList:
                if t.pos[1] > 230 and t.pos[1] > maxDis:
                    maxDis = t.pos[1]
                    maxColor = []
                    maxColor.append(t.color)
                elif t.pos[1] > 230 and t.pos[1] == maxDis:
                    maxDis = t.pos[1]
                    maxColor.append(t.color)

            if len(maxColor) > 0:
                run = Falseprint('The winner is: ')
