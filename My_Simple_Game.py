from tkinter import *
import random
win = Tk()

label1 = Label(win)
label2 = Label(win)

label3=Label(win,text='  Choose from below:  ')
label3.grid(row=3,column=0,sticky=N+S+E+W)

var=IntVar()
x = 1
colors=["blue violet","grey","blue","green","yellow","orange","red"]

cb2 = Checkbutton(win,text='Grey',variable=var,onvalue=1).grid(row=4,column=0)
cb3 = Checkbutton(win,text='Blue',variable=var,onvalue=2).grid(row=4,column=1)
cb4 = Checkbutton(win,text='Green',variable=var,onvalue=3).grid(row=4,column=2)
cb5 = Checkbutton(win,text='Yellow',variable=var,onvalue=4).grid(row=5,column=0)
cb6 = Checkbutton(win,text='Orange',variable=var,onvalue=5).grid(row=5,column=1)
cb7 = Checkbutton(win,text='Red',variable=var,onvalue=6).grid(row=5,column=2)

def checkans():
    global x
    global label2
    if(var.get() == x):
        label2 = Label(win,text='CORRECT',fg='black',bg='green').grid(row=6,column=0,sticky=N+S+E+W,columnspan=3)
    else:
        label2 = Label(win,text='WRONG',fg='black',bg='red').grid(row=6,column=0,sticky=N+S+E+W,columnspan=3)
    
def start():
    global x
    global label1
    global label2
    x = random.randint(1,6)
    label1 = Label(win,fg='black',text='Guess        This        Box\'s       Color')
    label1.config(bg = str(colors[x]))
    label1.grid(row=1,column=0,sticky=N+S+E+W,columnspan=10)
    label2 = Label(win,text='').grid(row=6,column=0,sticky=N+S+E+W,columnspan=3)

def quit1():
    win.destroy()

Button(win,text='Click to Generate a color: ',command = start).grid(row=0,column=0,columnspan=10)

Button(win,text='Check Answer', command = checkans).grid(row=7,column=0,columnspan=5)
Button(win,text='Quit', command = quit1).grid(row=7,column=1,columnspan=5)

win.resizable(False,False)
win.title('My small Game')
win.mainloop()
