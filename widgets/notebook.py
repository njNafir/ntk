from tkinter.ttk import Notebook as tkNotebook
from ntk.utils import *
from PIL import Image, ImageTk
from ntk.objects import gv
from tkinter import ttk as tkforstyle
from tkinter import TOP, PhotoImage

class Notebook:
    def __init__(self, root, class_="TNotebook", cursor="arrow", height=180, width=350, takefocus=0, padding=0, bg="bg-light", bd=0, fg="fg-dark", lightcolor="fg-info", row=0, column=0, sticky="wn", rowspan=1, columnspan=1, padx=1, pady=1, style=False, *args, **kwargs):
        super(Notebook, self).__init__(*args, **kwargs)
        bg = bg_colors()[bg] if bg in bg_colors() else bg
        fg = fg_colors()[fg] if fg in fg_colors() else fg
        lfg = fg_colors()[lightcolor] if lightcolor in fg_colors() else lightcolor

        self.main = tkNotebook(root, cursor=cursor, height=height, width=width, takefocus=takefocus, padding=padding)
        self.main.grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady)

        tfsty = tkforstyle.Style()
        self.style = style if style else "{}.TNotebook".format(self.main)
        self.tab_style = style + ".Tab" if style else "{}.TNotebook.Tab".format(self.main)
        tfsty.configure(self.tab_style, background=bg, foreground=fg, lightcolor=lfg, borderwidth=bd)

        if not style:
            tfsty.configure(self.style, background=bg, borderwidth=bd)

        self.main.config(style=self.style)

    def add(self, child, text, width=16, image=False, compound="left", underline=99, sticky="wn", padding=0):
        sp = ""
        for i in range(0, width-len(text) if width > len(text) else 1):
            sp = sp + " "

        self.main.add(child, text="{}{}{}".format(sp, text, sp), padding=padding, underline=underline, sticky=sticky, image=image, compound=compound)
