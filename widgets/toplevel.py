# Import Tkinter Toplevel to use it and modify default

from tkinter import Toplevel as tkToplevel

# Import all objects from snipp.objects

from snipp.objects import *

# Import all util from snipp.utils

from snipp.utils import *

class Toplevel(tkToplevel):

    # toplevel class can be called for create root

    # only one required field is root which is the any of widget
    # but if you don't want to pass root it will open as no relation
    # with main root tkinter class

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # toplevel design is custom and can be set twice
    # Tk instance will contain the base tkinter Toplevel instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter toplevel

    # so if it cause an error most probably it's getting from tkinter toplevel object
    # see your all arguments and keywords is supporting by Tk or tkinter toplevel

    def __init__(self,
                 root=None, # root is a master window to place this toplevel into it
                 title="Toplevel", # title to showing on top bar
                 bg="bg-white", # background color, default is bootstrap referenced white
                 bd=0, # border width
                 class_="Toplevel", # class is important when you want to inherit any design or some methods
                 colormap=False, # color map
                 container=0, # container
                 cursor="arrow", # cursor style for toplevel
                 height=480, # toplevel window height
                 width=360, # toplevel window width
                 highlightbackground="bg-light", # background color when toplevel is highlighted
                                                                            # default is bootstrap referenced light
                 highlightcolor="fg-dark", # foreground color when toplevel is highlighted
                                                                            # default is bootstrap referenced dark
                 highlightthickness=0, # thickness width of toplevel when highlighted
                 menu=False, # top level menu can be set with this command
                 padx=0, # grid padding left and right
                 pady=0, # grid padding top and bottom
                 relief="flat", # toplevel relief style
                 screen="", # toplevel screen
                 takefocus=1, # set if toplevel window can take focus or not
                 use=False, # use
                 visual=False, # visual
                 resize_x=0, # toplevel window resizing horizontally is allowed or not
                 resize_y=0, # toplevel window resizing vertically is allowed or not
                 x=False, # toplevel window positioning left right position
                 y=False, # toplevel window positioning top bottom position
                 topbar=True,
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        super(Toplevel, self).__init__(root,
                                       class_=class_,
                                       container=container,
                                       screen=screen,
                                       colormap=colormap if colormap else self, # see if colormap passed
                                                                                        # else set this object
                                       *args, **kwargs
                                    )

        # see if topbar is passed

        if not topbar:

            # if not topbar is allowed
            # disable top bar so top bar actions will be removed

            self.overrideredirect(True)

        # topbar geometry system to fit width and window
        # with referenced to main tkinter class
        # or sub window/widget

        # check if x is passed

        if not x:

            # if x is not passed
            # try to place this toplevel in
            # the middle of screen by horizontal

            x = int((gv.device_width-width)/2)


        # check if y is passed

        if not y:

            # if y is not passed
            # try to place this toplevel in
            # the middle of screen by vertical

            y = int((gv.device_height-height)/2)-32

        # next we will configure geometry manager
        # by x y and width height

        self.geometry("{}x{}+{}+{}".format(
                        width, # width of toplevel
                        height, # height of toplevel
                        x, # toplevel x position
                        y # toplevel y position
                    )
                )

        # set toplevel icon to global icon

        self.iconbitmap(gv.icon_path)

        # set toplevel resizable options
        # by toplevel.resizable(x, y)

        self.resizable(resize_x, resize_y)

        # set toplevel title to passed title

        self.title(title)

        # next we will configure some important parameters
        # so that our toplevel will ready to make
        # reference design

        self.config(
                background=color(bg), # color of background
                borderwidth=bd,
                cursor=cursor,
                height=height,
                width=width,
                highlightbackground=color(highlightbackground), # color of highlight background
                highlightcolor=color(highlightcolor), # color highlight foreground
                highlightthickness=highlightthickness,
                padx=padx,
                pady=pady,
                relief=relief,
                takefocus=takefocus
            )

        # check if menu is passed

        if menu:

            # if menu is passed then
            # configure toplevel menu into passed menu

            self.config(menu=menu)

        # check if visual is passed

        if visual:

            # if visual is passed then
            # configure toplevel visual into passed visual

            self.config(visual=visual)

        # check if use is passed

        if use:

            # if use is passed then
            # configure toplevel use into passed use

            self.config(use=use)
