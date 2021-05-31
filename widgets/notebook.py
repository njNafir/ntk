# Import Tcl Tkinter Notebook to use it and modify default

from tkinter.ttk import Notebook as tkNotebook

# Import all util from ntk.utils

from ntk.utils import *

# Import ttk from tkinter

from tkinter import ttk as tkforstyle

class Notebook(tkNotebook):

    # notebook class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # notebook design is custom and can be set twice
    # Notebook instance will contain the base tkinter notebook instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter notebook

    # so if it cause an error most probably it's getting from tkinter notebook object
    # see your all arguments and keywords is supporting by Notebook or tkinter notebook

    def __init__(self,
                 root, # root is a master window to place this notebook into it
                 class_="TNotebook", # notebook class to inherit object
                 cursor="arrow", # cursor style for notebook window
                 height=180, # notebook height
                 width=350, # notebook width
                 takefocus=0, # set notebook window can take focus or not
                 padding=0, # padding in square window
                 bg="bg-light", # background color, default is bootstrap referenced light
                 bd=0, # border width
                 fg="fg-dark", # foreground color, default is bootstrap referenced dark
                 lightcolor="fg-info", # light color, default is bootstrap referenced info
                 row=0, # grid row position
                 column=0, # grid column position
                 sticky="wn", # grid sticky position
                 rowspan=1, # grid row span width
                 columnspan=1, # grid column span width
                 padx=1, # grid padding left and right
                 pady=1, # grid padding top and bottom
                 style=False, # notebook default style
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        super(Notebook, self).__init__(root, # root is a master window to place this notebook into it
                                       cursor=cursor, # cursor style for notebook window
                                       height=height, # notebook height
                                       width=width, # notebook width
                                       takefocus=takefocus, # set notebook window can take focus or not
                                       padding=padding, # notebook window padding left right top bottom
                                       *args, **kwargs # extra arguments and keyword arguments
                                    )

        # background referenced color to standard color

        bg = color(bg)

        # foreground referenced color to standard color

        fg = color(fg)

        # light referenced color to standard color

        lfg = color(lightcolor)

        # self.main = tkNotebook(root,
        #                        cursor=cursor,
        #                        height=height,
        #                        width=width,
        #                        takefocus=takefocus,
        #                        padding=padding
        #                     )

        # notebook.grid automatically applied so
        # you don't need to recall it again
        # instead you can pass relative parameters
        # in notebook class

        self.grid(row=row, # grid row position
                  column=column, # grid column position
                  sticky=sticky, # grid sticky position
                  rowspan=rowspan, # grid row span position
                  columnspan=columnspan, # grid column span position
                  padx=padx, # grid padding left and right
                  pady=pady # grid padding top and bottom
            )

        # bind ttk style instance object
        # so that we can recall it

        tfsty = tkforstyle.Style()

        # check if style passed or create a style
        # with referenced by notebook class object

        self.style = style if style else "{}.TNotebook".format(self)

        # create notebook tab style
        # so every single tab will get a specific design

        self.tab_style = style + ".Tab" if style else "{}.TNotebook.Tab".format(self)

        # let's configure tab style to ttk style object
        # ttk.style.configure does that

        tfsty.configure(self.tab_style,
                        background=bg, # background color of notebook tab
                        foreground=fg, # foreground color of notebook tab
                        lightcolor=lfg, # light color of notebook tab
                        borderwidth=bd # border width of notebook tab
                    )

        if not style:

            # if not style passed create a style and
            # assign it/configure it to set it in ttk style

            tfsty.configure(self.style,
                            background=bg, # background color of notebook
                            borderwidth=bd # border width of notebook
                        )

        # let's add this style to our notebook by
        # notebook.config(style=style)

        self.config(style=self.style)

    def add(self, child, text, width=16, image=False, compound="left", underline=99, sticky="wn", padding=0):

        # notebook.add method is used to add a tab in notebook
        # it takes up most eight parameters

        # child is tab master window widget
        # text is to show up in tab button
        # width is tab button width
        # image is not used now but we can use it in future version
        # compound is used to separate text and image to left right top center
        # underline is used to set a text char position where a _ is inserted
        # sticky is grid sticky position
        # padding is applied to give padding around the tab window

        # set sp = "" initial variable

        sp = ""

        # iterate to give space to the left and right of the text
        # this text is tab button text

        for i in range(0, width-len(text) if width > len(text) else 1):

            # increase or join space until we are getting write space

            sp = sp + " "


        # at last we can add this tab in notebook window
        # notebook.add method is used to do that
        # so we are returning the super class method here

        return super(Notebook, self).add(child, # tab master window
                                         text="{}{}{}".format(sp, text, sp), # text with left and right separator
                                         padding=padding, # padding around tab window
                                         underline=underline, # underline position for tab text
                                         sticky=sticky, # tab sticky position
                                         image=image, # tab button image
                                         compound=compound # tab button image and text compounding
                                        )
