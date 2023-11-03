# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:08:42 2023

@author: cdren
"""

import turtle
import random
from array import array
import tkinter as tk
import tkinter.font as font

def flatoval(r):        # Horizontal Oval maker via sjaustirni of stackoverflow
    turtle.pensize(3)
    turtle.pen(pencolor="black")
    turtle.seth(-45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(.6*r,90)
        
# version with only2 main lines, on those lines and above top line
# version I have 
# version with 
# 1-1 
def noteGenr1(event):
    s= turtle.getscreen()
    t = turtle.Turtle()
    turtle.hideturtle()
    #t.reset()
    #t.clear()
    t.home()
    t.pen(pencolor="white")
    t.dot(5000)
    t.pen(pencolor="black")
    t.speed(0)
    t.up()
    t.pensize(8)
    t.goto(-300,100)
    t.down()
    t.goto(300,100) # draw first line 
    t.up()
    t.goto(-300,0)
    t.down()
    t.goto(300,0) # draw 2nd line 
    t.up() # lines are 600 pix long, 8 pix wide, and 125 pix apart 
    x_vals = array('f', [-225, -75, 75, 225]) # these always go in this order every time 
    y_options1 = array('f', [0, 100]) # on main 2 lines
    #vec = (1,2,3,4)
    #
    for i in range(0,4): # don't need 'end' to close for or if loops lol.       #  range() includes 1st arg but excludes 2nd, so 
        note = random.randint(0,1) # can only place notes in 2 y-locations       # this line means 0,1,2, or 3 but not 4
        t.up()
        xtemp = x_vals[i] # x position is first position, first num in x_vals vector
        ytemp = y_options1[note] # should be 
        t.goto(xtemp,ytemp)
        # t.down() not needed to draw dots 
        t.dot(100) # number is DIAMETER of dot 
        """  turtle.down()
        
        turtle.seth(-45)
        turtle.circle(50,90)
        turtle.circle(30,90)
        turtle.circle(50,90)
        turtle.circle(30,90)"""


# 1-2 
def noteGenr2(event):
    s= turtle.getscreen()
    t = turtle.Turtle()
    turtle.hideturtle()
    #t.reset()
    #t.clear()
    t.home()
    t.pen(pencolor="white")
    t.dot(5000)
    t.pen(pencolor="black")
    t.speed(0)
    t.up()
    t.pensize(8)
    t.goto(-300,100)
    t.down()
    t.goto(300,100) # draw first line 
    t.up()
    t.goto(-300,0)
    t.down()
    t.goto(300,0) # draw 2nd line 
    t.up() # lines are 600 pix long, 8 pix wide, and 125 pix apart 
    x_vals = array('f', [-225, -75, 75, 225]) # these always go in this order every time 
    y_options2 = array('f', [0, 100, 150]) # on main 2 + above top line 
    #vec = (1,2,3,4)
    #
    for i in range(0,4): # don't need 'end' to close for or if loops lol 
        note = random.randint(0,2)
        t.up()
        xtemp = x_vals[i] # x position is first position, first num in x_vals vector
        ytemp = y_options2[note] # should be 
        t.goto(xtemp,ytemp)
        # t.down() not needed to draw dots 
        t.dot(100) # number is DIAMETER of dot 



# 2-1 
def noteGenr3(event):
    s= turtle.getscreen()
    t = turtle.Turtle()
    turtle.hideturtle()
    #t.reset()
    #t.clear()
    t.home()
    t.pen(pencolor="white")
    t.dot(5000)
    t.pen(pencolor="black")
    t.speed(0)
    t.up()
    t.pensize(8)
    t.goto(-300,100)
    t.down()
    t.goto(300,100) # draw first line 
    t.up()
    t.goto(-300,0)
    t.down()
    t.goto(300,0) # draw 2nd line 
    t.up() # lines are 600 pix long, 8 pix wide, and 125 pix apart 
    x_vals = array('f', [-225, -75, 75, 225]) # these always go in this order every time 
    y_options3 = array('f', [-100, 0, 100, 150]) # on main 2 + above top + on 3rd lower line 
    #vec = (1,2,3,4)
    #
    for i in range(0,4): # don't need 'end' to close for or if loops lol 
        note = random.randint(0,3)
        t.up()
        xtemp = x_vals[i] # x position is first position, first num in x_vals vector
        if i==0 and y_options3[note] == -100: # if drawing 1st note AND randomNotePosition is going to be -100, aka y_options(0): 
            t.up()
            t.goto(-300,-100)
            t.down()
            t.goto(-150, -100)
            t.up()
            ytemp = y_options3[note]
            t.goto(xtemp,ytemp)
            t.dot(100) # number is DIAMETER of dot 
        else:
            note=random.randint(1,3) # can't index y_options(0), which would be the location/height of the 3rd low stubby line 
            ytemp = y_options3[note] # should be 
            t.goto(xtemp,ytemp)
        # t.down() not needed to draw dots 
            t.dot(100) # number is DIAMETER of dot 


# 2-2 
def noteGenr4(event):
    s= turtle.getscreen()
    t = turtle.Turtle()
    turtle.hideturtle()
    #t.reset()
    #t.clear()
    t.home()
    t.pen(pencolor="white")
    t.dot(5000)
    t.pen(pencolor="black")
    t.speed(0)
    t.up()
    t.pensize(8)
    t.goto(-300,100)
    t.down()
    t.goto(300,100) # draw first line 
    t.up()
    t.goto(-300,0)
    t.down()
    t.goto(300,0) # draw 2nd line 
    t.up() # lines are 600 pix long, 8 pix wide, and 125 pix apart 
    x_vals = array('f', [-225, -75, 75, 225]) # these always go in this order every time 
    y_options4 = array('f', [-100, -50, 0, 100, 150]) # these are randomized for each note # current one 
    #vec = (1,2,3,4)
    #
    for i in range(0,4): # don't need 'end' to close for or if loops lol 
        note = random.randint(0,4)
        t.up()
        xtemp = x_vals[i] # x position is first position, first num in x_vals vector
        if i==0 and y_options4[note] == -100:
            t.up()
            t.goto(-300,-100)
            t.down()
            t.goto(-150, -100)
            t.up()
            ytemp = y_options4[note]
            t.goto(xtemp,ytemp)
            t.dot(100) # number is DIAMETER of dot 
        else:
            note=random.randint(1,4)
            ytemp = y_options4[note] # should be 
            t.goto(xtemp,ytemp)
        # t.down() not needed to draw dots 
            t.dot(100) # number is DIAMETER of dot 



window = tk.Tk()

"""def handle_keypress(event):    # <- create an event handler 
    print(event.char) # print character associated to the key pressed 
window.bind("<Key>", handle_keypress) # bind keypress event to handle_keypress"""
# .bind always takes 2 arguments: event, and event handler. 
    # event is a string like "<event_name>"
    # event handler is name of funct to be called when event occurs 

f = font.Font(size = 18)    
button1 = tk.Button(text = "Generate Notes 1st-1", width=20,height=4,bg="black",fg="orange",)
button2 = tk.Button(text = "Generate Notes 1st-2", width=20,height=4,bg="black",fg="orange",)
button3 = tk.Button(text = "Generate Notes 2nd-1", width=20,height=4,bg="black",fg="orange",)
button4 = tk.Button(text = "Generate Notes 2nd-2", width=20,height=4,bg="black",fg="orange",)

button1['font'] = f
button2['font'] = f
button3['font'] = f
button4['font'] = f


button1.grid(row=1,column=1)
button2.grid(row=2,column=1)
button3.grid(row=1,column=2)
button4.grid(row=2,column=2)

"""
button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="right")
button4.pack(side="right")"""

button1.bind("<Button-1>",noteGenr1) # Button-1 here means left mouse button 
button2.bind("<Button-1>",noteGenr2)
button3.bind("<Button-1>",noteGenr3)
button4.bind("<Button-1>",noteGenr4)

# maybe define noteGenr as a function? and run it by clicking button? 



window.mainloop()  











