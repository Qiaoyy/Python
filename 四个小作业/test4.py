#coding=utf-8 
import Tkinter
import math
from Tkinter import Tk
def judge(event):
        x=(event.x-150)*(event.x-150)
        y=(event.y-100)*(event.y-100)
        k=math.sqrt(x+y)
        if k<=80:
            print("在")
        else:
            print("不在")

c = Tk()                                         
c.geometry('300x200')                
c.resizable(width=False, height=False) 
canvas = Tkinter.Canvas(bg="white", height=300, width=300)
oval = canvas.create_oval(70, 20, 230, 180, fill="red")
canvas.bind("<Button-1>",judge)
canvas.pack()
c.mainloop()
