# Import Tkinter Frame to use it and modify default

from tkinter import Frame as tkFrame

# Import all util from ntk.utils

from ntk.utils import *

class Frame(tkFrame):

    # frame class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # every design is custom and can be set twice
    # Frame instance will contain the base tkinter frame instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter frame

    # so if it cause an error most probably it's getting from tkinter frame object
    # see your all arguments and keywords is supporting by Frame or tkinter frame

    def __init__(self,
                 root, # root is a master window to place this frame into it
                 bg="bg-white", # background color, default is bootstrap referenced white
                 bd=0, # border width
                 colormap=None, # color map
                 class_=False, # class name to inherit styles and methods
                 container=0, # container
                 cursor="arrow", # mouse cursor style arrow hand2 etc
                 height=64, # frame height
                 highlightbackground="bg-light", # background color when frame is highlighted,
                                                                            # default is bootstrap referenced light
                 highlightcolor="bg-dark", # foreground color when frame is highlighted,
                                                                            # default is bootstrap referenced dark
                 highlightthickness=0, # thickness width when frame is highlighted
                 row=0, # grid row position
                 column=0, # grid column position
                 padx=0, # grid padding left and right
                 pady=0, # grid padding top and bottom
                 relief="flat", # relief style flat groove etc
                 sticky="w", # grid sticky position
                 takefocus=0, # set frame can take focus or not
                 visual=0, # visual
                 width=128, # frame width
                 gridrow=1, # grid row configure row weight
                 gridcolumn=1, # grid column configure column weight
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        super(Frame, self).__init__(
                                    root,
                                    class_=class_ if class_ else "Frame", # pass class if has else pass "Frame"
                                                                                    # which is tkinter default
                                    visual=visual,
                                    container=container,
                                    colormap=colormap,
                                    highlightbackground=color(highlightbackground), # background color when frame is
                                                                                        # highlighted
                                    highlightcolor=color(highlightcolor), # foreground color when frame is
                                                                                        # highlighted
                                    highlightthickness=highlightthickness,
                                    bg=color(bg), # color of background
                                    borderwidth=bd,
                                    cursor=cursor,
                                    height=height,
                                    relief=relief,
                                    takefocus=takefocus,
                                    # width=width
                                    *args, **kwargs
                                )

        # setting width by configure frame
        # because somehow passing it into super method
        # raising a error

        self.config(width=width)

        # frame grid configure automatically
        # so you don't need to call it again
        # but you can pass grid params in frame class

        self.grid(
                row=row, # grid row position
                column=column, # grid column position
                padx=padx, # grid padding left and right
                pady=pady, # grid padding top and bottom
                sticky=sticky # grid sticky position
            )

        # set grid column configure
        # so it will auto scale when
        # main window scaled

        root.grid_columnconfigure(
                column, # column configure column position
                weight=gridcolumn # grid weight of column
            )

        # set grid row configure
        # so it will auto scale when
        # main window scaled

        root.grid_rowconfigure(
                row, # row configure row position
                weight=gridrow # grid weight of row
            )
