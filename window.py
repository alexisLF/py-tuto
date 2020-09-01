import tkinter as tk

def create_window():
    tk.Toplevel(root)

root = tk.Tk()
b = tk.Button(root, text='Click to open a new window', command=create_window, font=('times', 40, 'bold'), bg='#3E4149')
b.pack()
root.mainloop()