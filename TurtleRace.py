#!/bin/python3

from turtle import *
from random  import randint


speed(10)
penup()
goto(-140, 140)


for step in range(10):
   write(step, align='center')
   right(90)
   forward(10)
   pendown()
   forward(150)
   penup()
   backward(160)
   left(90)
   forward(20)
   
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()


book = Turtle()
book.color('purple')
book.shape('turtle')

book.penup()
book.goto(-160,40)
book.pendown()

coffee = Turtle()
coffee.color('orange')
coffee.shape('turtle')

coffee.penup()
coffee.goto(-160,10)
coffee.pendown()



for turn in range(100):
  ada.forward(randint(1,7))
  bob.forward(randint(1,6))
  book.forward(randint(2,8))
  coffee.forward(randint(3,7))