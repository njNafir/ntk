from tkinter import Scrollbar as tkScrollbar
from ntk.utils import *

class Scrollbar(tkScrollbar):
    def __init__(self, root, scroll_on=False, orient="vertical", width=12, row=0, column=1, columnspan=1, padx=0, pady=0, sticky="ns", activebg="bg-light", activerelief="flat", bg="bg-dark", bd=0, command=False, cursor="arrow", elementborderwidth=0, highlightbg="bg-primary", highlightcolor="fg-dark", highlightthickness=1, jump=True, relief="flat", repeatdelay=300, repeatinterval=100, takefocus=1, troughcolor="fg-secondary", gridrow=1, gridcolumn=1, *args, **kwargs):

        super(Scrollbar, self).__init__(root, orient=orient, width=width, activebackground=color(activebg), activerelief=activerelief, bg=color(bg), bd=bd, cursor=cursor, elementborderwidth=elementborderwidth, highlightbackground=color(highlightbg), highlightcolor=color(highlightcolor), highlightthickness=highlightthickness, jump=jump, relief=relief, repeatdelay=repeatdelay, repeatinterval=repeatinterval, takefocus=takefocus, troughcolor=color(troughcolor), *args, **kwargs)

        self.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)

        root.grid_columnconfigure(column, weight=gridcolumn)
        root.grid_rowconfigure(row, weight=gridrow)

        if scroll_on:
            if orient == 'horizontal':
                self.config(command = scroll_on.xview)
                scroll_on.config(xscrollcommand = self.set)
            elif orient == 'vertical':
                self.config(command = scroll_on.yview)
                scroll_on.config(yscrollcommand = self.set)
