from tkinter import Frame as tkFrame
from tkinter.ttk import Frame as ttkFrame
from tkinter import ttk as ttkforstyle
from ntk.utils import *

class Frame(tkFrame):
    def __init__(self, root, bg="bg-white", bd=0, colormap=None, class_=False, container=0, cursor="arrow", height=64, highlightbackground="bg-light", highlightcolor="bg-dark", highlightthickness=0, row=0, column=0, padx=0, pady=0, relief="flat", sticky="w", takefocus=0, visual=0, width=128, gridrow=1, gridcolumn=1, *args, **kwargs):
        super(Frame, self).__init__(root, class_=class_ if class_ else "Frame", visual=visual, container=container, colormap=colormap, *args, **kwargs)

        class_ = class_ if class_ else "Frame"
        vis = visual if visual else 0
        cont = container if container else 0
        bg = color(bg)
        hlbg = color(highlightbackground)
        hcbg = color(highlightcolor)

        self.config(highlightbackground=hlbg, highlightcolor=hcbg, highlightthickness=highlightthickness, bg=bg, borderwidth=bd, cursor=cursor, height=height, relief=relief, takefocus=takefocus, width=width)

        self.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)

        root.grid_columnconfigure(column, weight=gridcolumn)
        root.grid_rowconfigure(row, weight=gridrow)
