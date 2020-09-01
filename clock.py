from tkinter import *
import time

root = Tk()
clock = Label(root, font=('times', 20, 'bold'), bg='red')
label = Label(root, text='Digital Clock', font=('times', 30, 'bold'))
label.pack()
clock.pack()


def tick():
    time2 = time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200, tick)


tick()
root.mainloop()
