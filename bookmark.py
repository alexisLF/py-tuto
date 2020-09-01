import tkinter as tk
import webbrowser
from functools import partial


def google():
    webbrowser.open('www.google.com', new=1)

def ytb():
    webbrowser.open('www.youtube.com', new=1)

def fb():
    webbrowser.open('www.facebook.com', new=1)

def amazon():
    webbrowser.open('www.amazon.com', new=1)

root = tk.Tk()
ytbI = tk.PhotoImage(file =r"ytb.png").subsample(10, 10)
aI = tk.PhotoImage(file =r"amazon.png").subsample(10, 10)
gI = tk.PhotoImage(file =r"google.png").subsample(10, 10)
fI = tk.PhotoImage(file =r"facebook.png").subsample(10, 10)

b1 = tk.Button(root, command=partial(google), image=gI)
b2 = tk.Button(root, command=partial(ytb), image=ytbI)
b3 = tk.Button(root, command=partial(fb), image=fI)
b4 = tk.Button(root, command=partial(amazon), image=aI)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
root.mainloop()