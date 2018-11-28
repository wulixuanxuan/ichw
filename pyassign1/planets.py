#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3

"""Planets.py: Description of what planets does.

__author__ = "YuQi Xuan"
__pkuid__  = "1800011787"
__email__  = "1800011787@pku.edu.cn"
"""


import turtle

import math

def main():
    
    wn=turtle.Screen()
    wn.bgcolor("black")

    sun=turtle.Turtle()
    sun.fillcolor("yellow")
    sun.shape("circle")
    sun.shapesize(2,2,2)
    sun.pencolor("yellow")

    Mercury = turtle.Turtle()      
    Mercury.color("blue")
    Mercury.up()
    Mercury.shape("circle")
    Mercury.shapesize(1)

    Venus = turtle.Turtle()      
    Venus.color("khaki")
    Venus.up()
    Venus.shape("circle")
    Venus.shapesize(1.4)

    Earth = turtle.Turtle()      
    Earth.color("LightSkyBlue")
    Earth.up()
    Earth.shape("circle")
    Earth.shapesize(1.6)

    Mars = turtle.Turtle()      
    Mars.color("Red")
    Mars.up()
    Mars.shape("circle")
    Mars.shapesize(1.2)

    Jupiter = turtle.Turtle()      
    Jupiter.color("burlywood")
    Jupiter.up()
    Jupiter.shape("circle")
    Jupiter.shapesize(2)

    Saturn = turtle.Turtle()      
    Saturn.color("medium springgreen")
    Saturn.up()
    Saturn.shape("circle")
    Saturn.shapesize(1.8)

    for i in range(1000):
        i=i/100
        Mercury.goto(30*(math.sin(6*i))-40*(math.cos(6*i)),30*(math.sin(6*i))+40*(math.cos(6*i)))
        Venus.goto(50*(math.sin(5*i))-60*(math.cos(5*i)),50*(math.sin(5*i))+60*(math.cos(5*i)))
        Earth.goto(70*(math.sin(4*i))-80*(math.cos(4*i)),70*(math.sin(4*i))+80*(math.cos(4*i)))
        Mars.goto(90*(math.sin(3*i))-100*(math.cos(3*i)),90*(math.sin(3*i))+100*(math.cos(3*i)))
        Jupiter.goto(110*(math.sin(2*i))-120*(math.cos(2*i)),110*(math.sin(2*i))+120*(math.cos(2*i)))
        Saturn.goto(130*(math.sin(i))-140*(math.cos(i)),130*(math.sin(i))+140*(math.cos(i)))
        Mercury.down()
        Venus.down()
        Earth.down()
        Mars.down()
        Jupiter.down()
        Saturn.down()



if __name__ == '__main__':
    main()
    

