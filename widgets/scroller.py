# Import Tkinter Scrollbar to use it and modify default

from tkinter import Scrollbar as tkScrollbar

# Import all util from ntk.utils

from ntk.utils import *

class Scrollbar(tkScrollbar):

    # scrollbar class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # scrollbar design is custom and can be set twice
    # Scrollbar instance will contain the base tkinter scrollbar instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter scrollbar

    # so if it cause an error most probably it's getting from tkinter scrollbar object
    # see your all arguments and keywords is supporting by Scrollbar or tkinter panedwindow

    def __init__(self,
                 root, # root is a master window to place this scrollbar into it
                 scroll_on=False, # set scroll on window/widget, set scroll effect on this window
                 orient="vertical", # scroll orient left-right or top-bottom
                 width=12, # scrollbar width
                 row=0, # grid row position
                 column=1, # grid column position
                 columnspan=1, # grid column span
                 padx=0, # grid padding left and right
                 pady=0, # grid padding top and bottom
                 sticky="ns", # grid sticky position
                 activebg="bg-light", # background color when scrollbar is active, default is bootstrap referenced light
                 activerelief="flat", # relief style when scrollbar is active
                 bg="bg-dark", # background color, default is bootstrap referenced dark
                 bd=0, # border width
                 # command=False,
                 cursor="arrow", # cursor style for scrollbar
                 elementborderwidth=0, # element border width
                 highlightbg="bg-primary", # background color when bar is highlighted, default is bootstrap ref primary
                 highlightcolor="fg-dark", # foreground color when bar is highlighted, default is bootstrap ref dark
                 highlightthickness=1, # bar thickness width when bar is highlighted
                 jump=True, # jump scrolling when clicked on bar
                 relief="flat", # relief style for bar
                 repeatdelay=300, # bar repeat delay
                 repeatinterval=100, # bar repeat interval
                 takefocus=1, # set if bar can take focus or not
                 troughcolor="fg-secondary", # bar trough color, default is bootstrap referenced secondary
                 gridrow=1, # grid configure row weight
                 gridcolumn=1, # grid configure column weight
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        super(Scrollbar, self).__init__(root,
                                        orient=orient,
                                        width=width,
                                        activebackground=color(activebg), # color of active background
                                        activerelief=activerelief,
                                        bg=color(bg), # color of background
                                        bd=bd,
                                        cursor=cursor,
                                        elementborderwidth=elementborderwidth,
                                        highlightbackground=color(highlightbg), # color of highlight background
                                        highlightcolor=color(highlightcolor), # color highlight foreground
                                        highlightthickness=highlightthickness,
                                        jump=jump,
                                        relief=relief,
                                        repeatdelay=repeatdelay,
                                        repeatinterval=repeatinterval,
                                        takefocus=takefocus,
                                        troughcolor=color(troughcolor), # color of trough color
                                        *args, **kwargs # extra arguments and keyword arguments
                                    )

        # grid is automatically applied
        # so you don't need to recall it again
        # instead you can pass related parameters
        # in scrollbar class init

        self.grid(
                row=row, # grid row position
                column=column, # grid column position
                columnspan=columnspan, # grid column span
                padx=padx, # grid padding left and right
                pady=pady, # grid padding top and bottom
                sticky=sticky # grid sticky position
            )

        # grid column configure set for
        # getting scaled column width
        # dynamically

        # it will scale up your window as responsive

        root.grid_columnconfigure(
                column, # grid column position in root
                weight=gridcolumn # grid column weight
            )

        # grid row configure set for
        # getting scaled row width
        # dynamically

        # it will scale up your window as responsive

        root.grid_rowconfigure(
                row, # grid row position in root
                weight=gridrow # grid row weight
            )

        # check if scroll on master defined

        if scroll_on:

            # check if orient is horizontal or vertical

            if orient == 'horizontal':

                # if orient is horizontal then configure scroll bar command into xview

                self.config(command=scroll_on.xview)

                # also config scroll on x scroll command to scrollbar

                scroll_on.config(xscrollcommand=self.set)

            elif orient == 'vertical':

                # if orient is vertical then configure scroll bar command into yview

                self.config(command=scroll_on.yview)

                # also config scroll on y scroll command to scrollbar

                scroll_on.config(yscrollcommand=self.set)
