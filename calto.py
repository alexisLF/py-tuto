import tkinter
from functools import partial

root = tkinter.Tk()
root.iconbitmap('icon-icons.ico')

def createCalculator():
    screenFrame = tkinter.Frame()
    padFrame = tkinter.Frame()
    screenFrame.pack()
    equalFrame = tkinter.Frame()
    padFrame.pack()
    equalFrame.pack()
    myTup = ('7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '.', 'C', '/')
    w = 0
    stg = tkinter.StringVar()
    tkinter.Label(screenFrame, textvariable=stg, relief=tkinter.SUNKEN, width=20).grid(row=0, column=1)
    for j in range(4):
        for i in range(4):
            if myTup[w] != 'C':
                tkinter.Button(padFrame, text=myTup[w], width=4, height=3, command=partial(addToStg, stg, myTup[w])).grid(row=j + 1,
                                                                                                             column=i)
            else:
                tkinter.Button(padFrame, text=myTup[w], width=4, height=3,
                               command=partial(clear, stg)).grid(row=j + 1,
                                                                              column=i)
            w += 1
    tkinter.Button(equalFrame, text="=", width=20, command=partial(calculate, stg)).grid(row=0)


def addToStg(stg, elem):
    stg.set(stg.get() + elem)


def calculate(stg):
    stg.set(eval(stg.get()))

def clear(stg):
    stg.set('')

createCalculator()

root.mainloop()