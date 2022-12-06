import turtle
from turtle import *
color('red', 'black')
turtle.speed('fast')
fillcolor('blue')
begin_fill()


while True:
    forward(100)
    left(90)
    
    if abs(pos()) < 1:
        break

color('green','black')
while True:
    
    forward(100)
    right(90)
    
    
    if abs(pos()) < 1:
        break
        end_fill()
color('red', 'black')        
while True:
    backward(100)
    left(90)
    
    if abs(pos()) < 1:
        break
        end_fill()

color('green','yellow')
while True:
    
    backward(100)
    right(90)
    
    if abs(pos()) < 1:
        break
        end_fill()
 
end_fill()
done()
