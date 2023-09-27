'''
import turtle
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('blue')
pokey = turtle.Turtle()
pokey.shape('turtle')
pokey.color('red')
def make_square(the_turtle):
    for i in range(0, 4):
        the_turtle.forward(100)
        the_turtle.right(90)
def make_spiral(the_turtle):
    for i in range(0, 36):
        make_square(the_turtle)
        the_turtle.right(10)
make_spiral(slowpoke)
pokey.right(5)
make_spiral(pokey)

'''
'''
#Star
import turtle
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.color('blue')
for i in range(5):
    slowpoke.forward(100)
    slowpoke.right(144)
'''

'''
import turtle
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
slowpoke.pencolor('blue')
slowpoke.penup()
slowpoke.setposition(-120, 0)
slowpoke.pendown()
slowpoke.circle(50)
slowpoke.pencolor('red')
slowpoke.penup()
slowpoke.setposition(120, 0)
slowpoke.pendown()
slowpoke.circle(50)

'''
'''
import turtle
slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
def make_shape(t, sides):
    angle = 360/sides
    for i in range(0, sides):
        t.forward(100)
        t.right(angle)
make_shape(slowpoke, 3)
make_shape(slowpoke, 5)
make_shape(slowpoke, 8)
make_shape(slowpoke, 10)

'''
'''
import turtle
slowpoke = turtle.Turtle()
#slowpoke.turn(90)
slowpoke.forward(100)
slowpoke.shape('turtle')
print(slowpoke.shape)
slowpoke.shape('circle')
print(slowpoke.shape())
'''

mylist = list()
mylist.append('first')
mylist.append('second')
mylist.reverse()
print(mylist)

greeting = str('hello reader')
shout = greeting.upper()
print(shout)

pi = float(3.1415)
is_int = pi.is_integer()
print(pi, is_int)