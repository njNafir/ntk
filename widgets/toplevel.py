from tkinter import Toplevel as tkToplevel, Label
from ntk.objects import *
from ntk.utils import *

class Toplevel(tkToplevel):
    def __init__(self, root=None, title="Toplevel", bg="bg-white", bd=0, class_="Toplevel", colormap=False, container=0, cursor="arrow", height=480, width=360, highlightbackground="bg-light", highlightcolor="fg-dark", highlightthickness=0, menu=False, padx=0, pady=0, relief="flat", screen="", takefocus=1, use=False, visual=False, resize_x=0, resize_y=0, x=False, y=False, *args, **kwargs):

        super(Toplevel, self).__init__(root, class_=class_, container=container, screen=screen, colormap=colormap if colormap else self, *args, **kwargs)

        if not title:
            self.overrideredirect(True)

        self.geometry("{}x{}+{}+{}".format(width, height, x if x else int((gv.device_width-width)/2), y if y else int((gv.device_height-height)/2)-32))
        self.iconbitmap(gv.icon_path)
        self.resizable(resize_x, resize_y)

        self.title(title)
        self.config(background=color(bg), borderwidth=bd, cursor=cursor, height=height, width=width, highlightbackground=color(highlightbackground), highlightcolor=color(highlightcolor), highlightthickness=highlightthickness, padx=padx, pady=pady, relief=relief, takefocus=takefocus)

        if menu: self.config(menu=menu)
        if visual: self.config(visual=visual)
        if use: self.config(use=use)
