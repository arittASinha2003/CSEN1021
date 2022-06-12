import turtle
wn = turtle.Screen()
wn.setup(width = 600, height = 600)
red = turtle.Turtle()
red.speed(0)

def curve():
  for i in range (200):
    red.right(1)
    red.forward(1)

def heart():
  red.fillcolor('red')
  red.begin_fill()
  red.left(140)