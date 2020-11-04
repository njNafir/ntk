from tkinter import PanedWindow as tkPanedWindow
from tkinter.ttk import PanedWindow as ttkPanedWindow
from tkinter import ttk as ttkforstyle
from ntk.utils import *

class PanedWindow(tkPanedWindow):
    def __init__(self, root, bg="bg-light", bd=2, cursor="arrow", handlepad=0, handlesize=0, height=370, opaqueresize=0, orient="vertical", relief="flat", sashcursor="sizing", sashpad=0, sashrelief="flat", sashwidth=4, showhandle=True, width=370, row=0, column=0, rowspan=1, columnspan=1, padx=(0, 0), pady=(0, 0), ipady=0, sticky="wsen", gridrow=1, gridcolumn=1, *args, **kwargs):
        super(PanedWindow, self).__init__(root, orient=orient, bg=color(bg), bd=bd, handlepad=handlepad, handlesize=handlesize, opaqueresize=opaqueresize, relief=relief, sashcursor=sashcursor, sashpad=sashpad, sashrelief=sashrelief, sashwidth=sashwidth, showhandle=showhandle, width=width-10, *args, **kwargs)

        self.config(cursor=cursor, height=height)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, ipady=ipady, sticky=sticky)

        root.grid_columnconfigure(column, weight=gridcolumn)
        root.grid_rowconfigure(row, weight=gridrow)
