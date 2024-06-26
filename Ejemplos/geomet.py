import turtle 
import tkinter as TK
import tkinter

t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor('black')

t.width(2)
t.speed(15)

color=('white', 'pink', 'cyan')

for i in range (300):
    t.pencolor(color[i%3])
    t.forward(i*4)
    t.right(121)