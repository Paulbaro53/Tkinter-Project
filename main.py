from tkinter import *
import time
import random

root=Tk()
root.geometry("600x400")

w = 600
h = 400
x=w // 2
y=h // 2

can=Canvas(root,width=w, height=h, bg='black')
can.pack()

my_chr=can.create_rectangle(x,y,x+20,y+20, outline="red")

#Movement functions
def left(event):
    x =- 10
    y = 0
    can.move(my_chr,x,y)

def right(event):
    x=10
    y=0
    can.move(my_chr,x,y)
    
def up(event):
    x=0
    y=-10
    can.move(my_chr,x,y)

def down(event):
    x=0
    y=10
    can.move(my_chr,x,y)

#event handelers
root.bind('<Left>',left)
root.bind('<Right>',right)
root.bind('<Up>',up)
root.bind('<Down>',down)

can.coords(my_chr, 100, 350, x-50, y-50)

#Line1
can.create_line(600,350,-100,350,fill="white")
#Line2
can.create_line(600,250,-100,250,fill="white")


root.mainloop()
