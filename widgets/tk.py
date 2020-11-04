from tkinter import Tk as tTk
from ntk.objects import *
from ntk.utils import *
import os
from ntk.widgets.panedwindow import PanedWindow

base_var()

class Tk(tTk):
    def __init__(self, title="Main Window", resize_x=True, resize_y=True, width=360, height=380, x=False, y=False, state="normal", bg="bg-white", icon=False, mainframe=True, fullscreen=False, gridrow=1, gridcolumn=1, *args, **kwargs):
        super(Tk, self).__init__(*args, **kwargs)

        if not title:
            self.overrideredirect(True)

        else:
            gv.main_window = self.main = self
            gv.device_width 	= self.winfo_screenwidth()
            gv.device_height 	= self.winfo_screenheight()

            gv.wpc      = gv.device_width/1366
            gv.hpc      = gv.device_height/768

        if fullscreen:
            self.geometry("{}x{}".format(gv.device_width, gv.device_height))
            self.state("zoomed")
        else:
            self.geometry("{}x{}+{}+{}".format(width, height, (int(gv.device_width/2) - int(width/2)) if not x else x, (int(gv.device_height/2) - int(height/2))-48 if not y else y))

        self.iconbitmap(icon if icon else os.path.join(os.path.dirname(os.path.dirname(__file__)), "icon.ico"))
        self.title(title)

        self.resizable(resize_x, resize_y)
        self.state(state)
        self.configure(background=color(bg))

        if mainframe:
            self.mainframe = PanedWindow(self, bg="bg-dark")

            self.grid_rowconfigure(0, weight=gridrow)
            self.grid_columnconfigure(0, weight=gridcolumn)
