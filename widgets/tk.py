# Import Tkinter Tk to use it and modify default

from tkinter import Tk as tTk

# Import all objects from ntk.objects

from ntk.objects import *

# Import all util from ntk.utils

from ntk.utils import *

# Import os

import os

# Import ntk PanedWindow to use it as default middle window

from ntk.widgets.panedwindow import PanedWindow
from tkinter import font

# set base global variable so we can use these next time

base_var()

class Tk(tTk):

    # tk class can be called for create root tk
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # tk design is custom and can be set twice
    # Tk instance will contain the base tkinter Tk instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter tk

    # so if it cause an error most probably it's getting from tkinter tk object
    # see your all arguments and keywords is supporting by Tk or tkinter tk

    def __init__(self,
                 title="Main Window", # title to showing on top bar
                 resize_x=True, # resize x is to set horizontal resizable
                 resize_y=True, # resize y is to set vertical resizable
                 width=360, # tkinter window width
                 height=380, # tkinter window height
                 x=False, # tkinter window positioning root x
                 y=False, # tkinter window positioning root y
                 state="normal", # tkinter window state
                 bg="bg-white", # background of tkinter window, default is bootstrap referenced white
                 icon=False, # tkinter window icon
                 mainframe=True, # set if tkinter hold a main frame window or not
                 fullscreen=False, # set if you want to set this window to full window
                 gridrow=1, # grid configure row position
                 gridcolumn=1, # grid configure column position
                 topbar=True,
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        super(Tk, self).__init__(*args, **kwargs)

        # check if top bar is passed and it's False

        if not topbar:

            # if top bar is False, then we don't want to show up the top bar row

            self.overrideredirect(True)

        else:

            # set this tkinter window object to global var main window

            gv.main_window = self.main = self

            # count monitor screen width and set it to global var

            gv.device_width = self.winfo_screenwidth()

            # count monitor screen height and set it to global var

            gv.device_height = self.winfo_screenheight()

            # count width per cell by dividing
            # screen full width by most possible
            # screen width to fit most general
            # case of screen width

            gv.wpc = gv.device_width/1366

            # count height per cell by dividing
            # screen full width by most possible
            # screen height to fit most general
            # case of screen height

            gv.hpc = gv.device_height/768

        # check if full screen call is passed

        if fullscreen:

            # change geometry of tkinter window to
            # fit into full screen

            self.geometry("{}x{}".format(
                                    gv.device_width, # width param
                                    gv.device_height # height param
                                )
                            )

            # change state of tkinter window to zoomed
            # so it will force fit to screen

            # self.state("zoomed")

        else:

            # check if x is passed

            if not x:

                # if x is not passed, then x can be middle point of screen width
                # so we are calculating and setting middle point

                x = (int(gv.device_width/2) - int(width/2))

            # check if y is passed

            if not y:

                # if y is not passed, the y can be middle point of screen width
                # so we are calculating and setting middle point

                y = (int(gv.device_height/2) - int(height/2))-48

            # next we can set x y with width and height to geometry

            self.geometry("{}x{}+{}+{}".format(
                                    width, # width of tkinter window if passed or default
                                    height, # height of tkinter window if passed or default
                                    x, # left position of screen
                                    y # bottom position of screen
                                )
                            )

        # check if icon is defined or not

        if not icon:

            # if icon not passed, we can set a default icon in ntk
            # as tkinter window icon

            icon = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icon.ico")

        # next we will set this icon in tkinter window top left

        # self.iconbitmap(icon)

        # set window title

        self.title(title)

        # set resizable by horizontal and vertical width
        # by setting tk.resizable(x, y)

        self.resizable(resize_x, resize_y)

        # set tkinter window state now

        self.state(state)

        # configure tkinter window background color

        self.configure(
                background=color(bg) # color of background
            )

        # check if middle frame is allowed or not

        if mainframe:

            # if middle frame is allowed,
            # let's create a middle frame for tkinter window

            # we are assigning panedwindow as middle frame

            # if you don't want to set it
            # you can call tk as mainframe=False
            # so it will not create mainframe for you
            # and you can create your desired
            # window or widget next time

            self.mainframe = PanedWindow(self, bg="bg-dark")

            # set grid configure row
            # you can pass weight as gridrow any value
            # and it will be set in it

            self.grid_rowconfigure(0, weight=gridrow)

            # set grid configure column
            # you can pass weight as gridcolumn any value
            # and it will be set in it

            self.grid_columnconfigure(0, weight=gridcolumn)
