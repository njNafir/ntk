# Import Tkinter PanedWindow to use it and modify default

from tkinter import PanedWindow as tkPanedWindow

# Import all util from ntk.utils

from ntk.utils import *

class PanedWindow(tkPanedWindow):

    # panedwindow class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # panedwindow design is custom and can be set twice
    # PanedWindow instance will contain the base tkinter panedwindow instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter panedwindow

    # so if it cause an error most probably it's getting from tkinter panedwindow object
    # see your all arguments and keywords is supporting by PanedWindow or tkinter panedwindow

    def __init__(self,
                 root, # root is a master window to place this panedwindow into it
                 bg="bg-light", # background color, default is bootstrap referenced light
                 bd=2, # border width
                 cursor="arrow", # cursor style for paned window
                 handlepad=0, # panedwindow subwidgets handling bar, this also work as bar width
                 handlesize=0, # panedwindow subwidgets handling bar, this also work as bar width
                 height=370, # panedwindow height
                 opaqueresize=0, # opaque resize
                 orient="vertical", # panedwindow subwidgets orientation
                 relief="flat", # panedwindow relief style flat groove etc
                 sashcursor="sizing", # panedwindow subwidgets handling sash bar cursor
                 sashpad=0, # panedwindow subwidgets handling sash bar show or hide
                 sashrelief="flat", # panedwindow subwidgets handling sash bar relief
                 sashwidth=4, # panedwindow subwidgets handling sash bar width
                 showhandle=True, # sash handle with handle pad
                 width=370, # panedwindow width
                 row=0, # grid row position
                 column=0, # grid column position
                 rowspan=1, # grid row span width
                 columnspan=1, # grid column span width
                 padx=(0, 0), # grid padding left and right
                 pady=(0, 0), # grid padding top and bottom
                 ipady=0, # grid internal padding top and bottom
                 sticky="wsen", # grid sticky position
                 gridrow=1, # grid configure row config weight
                 gridcolumn=1, # grid configure column config weight
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        super(PanedWindow, self).__init__(root,
                                          orient=orient,
                                          bg=color(bg), # color of background
                                          bd=bd,
                                          handlepad=handlepad,
                                          handlesize=handlesize,
                                          opaqueresize=opaqueresize,
                                          relief=relief,
                                          sashcursor=sashcursor,
                                          sashpad=sashpad,
                                          sashrelief=sashrelief,
                                          sashwidth=sashwidth,
                                          showhandle=showhandle,
                                          width=width-10,
                                          *args, **kwargs
                                    )

        # cursor and height attributes is not accepting by class init
        # so we can configure it

        self.config(
                cursor=cursor, # cursor style for panedwindow
                height=height # height of panedwindow
            )

        # panedwindow grid system will be automatically
        # applied so you don't need to
        # recall it again
        # but you can pass related parameters
        # in panedwindow class init

        self.grid(
                row=row, # grid row position
                column=column, # grid column position
                rowspan=rowspan, # grid row span
                columnspan=columnspan, # grid column span
                padx=padx, # grid padding left and right
                pady=pady, # grid padding top and bottom
                ipady=ipady, # grid internal padding top and bottom
                sticky=sticky # grid sticky position
            )

        # grid column weight configure
        # it will configure panedwindow
        # for setting it in root window
        # as auto scaling feature

        root.grid_columnconfigure(
                column, # grid column in root
                weight=gridcolumn # column configure weight
            )

        # grid row weight configure
        # it will configure panedwindow
        # for setting it in root window
        # as auto scaling feature

        root.grid_rowconfigure(
                row, # grid row in root
                weight=gridrow # row configure weight
            )
