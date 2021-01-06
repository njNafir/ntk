# Import Tkinter Canvas to use it and modify default

from tkinter import Canvas as tkCanvas

# Import all util from ntk.utils

from ntk.utils import *

# Import pyperclip
# pyperclip is used to copy and paste canvas element text when it's selected

try:
    import pyperclip
except:
    print('pyperclip not found, it can be installed by\npip install pyperclip')

class Canvas(tkCanvas):

    # canvas class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # every design is custom and can be set twice
    # Canvas instance will contain the base tkinter canvas instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter canvas

    # so if it cause an error most probably it's getting from tkinter canvas object
    # see your all arguments and keywords is supporting by ntk Canvas or tkinter canvas

    def __init__(self,
                 root, # root is a master window to place this button into it
                 bg="bg-white", # background color
                 highlightbackground="bg-white", # background color when canvas is highlighted
                 highlightcolor="fg-dark", # foreground color when canvas is highlighted
                 selectbackground="bg-primary", # element background color when canvas element is selected
                 scrollregion=[0,0,350,96], # [x1, y1, x2, y2] region when canvas is scrolling via scrollbar or mouse
                 relief="flat", # relief design can be flat, groove etc
                 width=350, # canvas width
                 height=96, # canvas height
                 row=0, # row position
                 column=0, # column position
                 rowspan=1, # row spanning size
                 columnspan=1, # column spanning size
                 padx=1, # padding in left and right
                 pady=1, # padding in top and bottom
                 mousescroll=True, # set False if you don't want to scrolling when scrolling via mouse
                 gridcolumn=1, # set 0 if you don't want responsiveness by column in it's root window
                 gridrow=1, # set 0 if you don't want responsiveness by row in it's root window
                 *args, **kwargs # extra arguments and keyword arguments can be passed
            ):

        super(Canvas, self).__init__(root,
                                     width=width,
                                     height=height,
                                     scrollregion=scrollregion,
                                     relief=relief,
                                     background=color(bg), # color of background
                                     highlightbackground=color(highlightbackground), #color of background when canvas
                                                                                                        # highlighted
                                     highlightcolor=color(highlightcolor), #color of foreground when canvas
                                                                                                        # highlighted
                                     selectbackground=color(selectbackground), #color of background when canvas
                                                                                                        # selected
                                     *args, **kwargs # extra arguments and keyword arguments will passed
                                )

        # scroll region x1
        # scroll region y1
        # scroll region x2
        # scroll region y2

        self.scr_x1, \
        self.scr_y1, \
        self.scr_x2, \
        self.scr_y2 = scrollregion

        self.grid(
                row=row, # grid configure row
                column=column, # grid configure column
                rowspan=rowspan, # grid configure row span
                columnspan=columnspan, # grid configure column span
                padx=padx, # grid configure padding left and right
                pady=pady # grid configure padding top and bottom
            )

        if mousescroll:
            self.bind("<MouseWheel>", lambda e: self.mousewheel(e)) # canvas scrolling by mouse scrolling

        self.bind("<Double-Button-1>", lambda e: self.select_clicked(e)) # canvas mouse double click selection command

        # canvas column configure by grid column

        root.grid_columnconfigure(
                                    column, # column position
                                    weight=gridcolumn # column weight
                                )

        root.grid_rowconfigure(
                                row, # row position
                                weight=gridrow # row weight
                            )

    def select_clicked(self, e=None):

        # check if clicked object is a text containing object

        if self.type("current") != "text":

            # if not clicked object is a text containing object then return

            return

        # canvas.focus_set()
        # can be used to focus in a canvas main widget

        self.focus_set() # set focus into clicked object from anywhere

        # canvas.focus(object)
        # can be used to focus in a specific object

        self.focus("current") # set focus into current object from anywhere

        # canvas.select_from(object, position)
        # can be used to select from this position

        self.select_from("current", 0) # select starting from 0 index from current clicked object

        # canvas.select_to(object, position)
        # can be used to select until this position

        self.select_to("current", "end") # select end to 'end' index from current clicked object

        # and at last copy to clipboard selected text from current object

        # pyperclip.copy function can be used for selecting any text
        # we are passing our selected text here

        # canvas.selection_get() method will return
        # current selected text from this canvas

        self.bind("<Control-c>", lambda e: pyperclip.copy(
                                                    "{}".format(
                                                        self.selection_get()
                                                    )
                                                )
                                            )

    def mousewheel(self, e):

        # mousewheel method is used to scroll
        # in canvas when mouse scrolled

        self.yview_scroll(
                    int(-1*(e.delta/120)), # get and set delta event into into with dividing by 120
                    "units" # set size into units
                )

    def increase_scrollragion(self, x1=False, y1=False, x2=False, y2=False):

        # canvas.increase_scrollregion(x1, y1, x2, y2) is used to
        # increase scrollregion size of a canvas window

        # scroll region x1
        # scroll region y1
        # scroll region x2
        # scroll region y2

        self.scr_x1, \
        self.scr_y1, \
        self.scr_x2, \
        self.scr_y2 = self.scr_x1 + (x1 if x1 else 0), \
                      self.scr_y1 + (y1 if y1 else 0), \
                      self.scr_x2 + (x2 if x2 else 0), \
                      self.scr_y2 + (y2 if y2 else 0)

        # at last set new scroll region in canvas
        # canvas.config(scrollregion=[x1, y1, x2, y2])

        self.config(
                scrollregion=[
                            self.scr_x1, # x1 position in region
                            self.scr_y1, # y1 position in region
                            self.scr_x2, # x2 position in region
                            self.scr_y2 # y2 position in region
                        ]
                    )

    def decrease_scrollragion(self, x1=False, y1=False, x2=False, y2=False):

        # canvas.decrease_scrollragion(x1, y1, x2, y2) is used to
        # decrease scrollregion size of a canvas window

        # scroll region x1
        # scroll region y1
        # scroll region x2
        # scroll region y2

        self.scr_x1, \
        self.scr_y1, \
        self.scr_x2, \
        self.scr_y2 = self.scr_x1 - (x1 if x1 else 0), \
                      self.scr_y1 - (y1 if y1 else 0), \
                      self.scr_x2 - (x2 if x2 else 0), \
                      self.scr_y2 - (y2 if y2 else 0)


        # at last set new scroll region in canvas
        # canvas.config(scrollregion=[x1, y1, x2, y2])

        self.config(
                scrollregion=[
                            self.scr_x1, # x1 position in region
                            self.scr_y1, # y1 position in region
                            self.scr_x2, # x2 position in region
                            self.scr_y2 # y2 position in region
                        ]
                    )
