import turtle
import random


turtle.circle(20)
answer = ''
while answer != 'N':
    answer = turtle.textinput("Paint circle", "Y/N")
    if answer == 'Y':
        turtle.goto()
        turtle.circle(random.randrange(1, 100))
    else:
        pass
