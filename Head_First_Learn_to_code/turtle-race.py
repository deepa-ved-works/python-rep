'''
import turtle
import random
turtles = list()
def setup():
    global turtles
    startline = -480
    # Y positions
    turtle_ycor = [-40, -20, 0, 20, 40, 60]
    # turtle color
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green', 'pink']
    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        turtles.append(new_turtle)
setup()
turtle.mainloop()

'''
'''
import turtle
import random
turtles = list()
def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')
    # Y positions
    turtle_ycor = [-40, -20, 0, 20, 40, 60]
    # turtle color
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green', 'pink']
    for i in range(0, len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)

def race():
    global turtles
    winner = False
    finishline = 590
    while not winner:
        for current_turtle in turtles:
            move = random.randint(0,2)
            current_turtle.forward(move)
            xcor = current_turtle.xcor()
            if(xcor >= finishline):
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0])
setup()
race()
turtle.mainloop()
'''


import turtle
import random
turtles = list()
class SuperTurtle(turtle.Turtle):
    def forward(self, distance):
        cheat_distance = distance + 5
        turtle.Turtle.forward(self, cheat_distance)

def setup():
    global turtles
    startline = -620
    screen = turtle.Screen()
    screen.setup(1290, 720)
    screen.bgpic('pavement.gif')
    # Y positions
    turtle_ycor = [-40, -20, 0, 20, 40, 60]
    # turtle color
    turtle_color = ['blue', 'red', 'purple', 'brown', 'green', 'pink']
    for i in range(0, len(turtle_ycor)):
        if i == 5:
            new_turtle = SuperTurtle()
        else:
            new_turtle = turtle.Turtle()
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        new_turtle.pendown()
        turtles.append(new_turtle)

def race():
    global turtles
    winner = False
    finishline = 590
    while not winner:
        for current_turtle in turtles:
            move = random.randint(0,2)
            current_turtle.forward(move)
            xcor = current_turtle.xcor()
            if(xcor >= finishline):
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0])
setup()
race()
turtle.mainloop()
