import tkinter as tk
from tkinter import font
from functools import partial


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init()

    def init(self):
        self.pack()
        self.create_screen()
        self.create_pad()

    def create_pad(self):
        self.pad = tk.Frame(self)
        self.create_numpad()
        self.create_operation()
        self.create_option()
        self.pad.pack()


    def create_screen(self):
        self.screen = tk.Frame(self)
        self.eval = tk.StringVar()
        self.result = tk.StringVar()
        tk.Label(self.screen, textvariable=self.result, relief=tk.SUNKEN, anchor=tk.E, width=30, height=4).grid(row=0, column=1)
        tk.Label(self.screen, textvariable=self.eval, relief=tk.SUNKEN, anchor=tk.E, width=30, height=4).grid(row=1, column=1)
        self.screen.pack()

    def create_numpad(self):
        _col = 1
        _row = 4
        for _number in range(0, 10):
            _tmp = tk.Button(self.pad,
                             text=_number, width=4, height=4,
                             command=partial(self._add_to_eval, _number))
            _tmp.grid(row=_row, column=_col, sticky=tk.N+tk.S+tk.E+tk.W)
            if _number == 0:
                _col += 1

            _col += 1
            if _col >= 3:
                _col = 0
                _row -= 1

        tk.Button(self.pad,
                  text=".", width=4, height=4,
                  command=partial(self._add_to_eval, ".")).grid(row=4, column=2, sticky=tk.N+tk.S+tk.E+tk.W)

    def create_operation(self):
        _operation_list = ["%", "/", "*", "**", "-", "+"]
        _row = 1
        _col = 3
        for _operation in _operation_list:
            _tmp = tk.Button(self.pad,
                             text=_operation, width=4, height=4,
                             command=partial(self._add_to_eval, _operation))
            _tmp.grid(row=_row, column=_col, sticky=tk.N+tk.S+tk.E+tk.W)
            _col += 1
            if _col > 4:
                _col = 3
                _row += 1

    def create_option(self):

        tk.Button(self.pad,
                  text="C", width=4, height=4,
                  command=self._clear_eval).grid(row=4, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        tk.Button(self.pad,
                  text="=", width=4, height=4,
                  command=self._calc_eval).grid(row=4, column=3, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)

    def _add_to_eval(self, elem):
        self.eval.set("{}{}".format(self.eval.get(), elem))

    def _remove_last(self):
        self.eval.set(self.eval.get()[:-1])

    def _clear_eval(self):
        self.eval.set("")

    def _clear_all(self):
        self.eval.set("")
        self.result.set("")

    def _calc_eval(self):
        self.result.set(eval(self.eval.get()))


root = tk.Tk()
root.resizable(100, 100)
app = Application(master=root)
app.mainloop()
