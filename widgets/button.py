# Import Tkinter Button to use it and modify default

from tkinter import Button as tkButton

# Import all util from ntk.utils

from ntk.utils import *

class Button(tkButton):

    # button class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # every design is custom and can be set twice
    # Button instance will contain the base tkinter button instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter button

    # so if it cause an error most probably it's getting from tkinter button object
    # see your all arguments and keywords is supporting by ntk Button or tkinter button

    def __init__(self,
                 root, # root is a master window to place this button into it
                 abg="bg-secondary", # background color when button is active
                 afg="fg-light", # foreground color when button is active
                 anchor="center", # anchor text to left right or center
                 bg="bg-info", # background color
                 bitmap=None, # bitmap image to place
                 bd=0, # border width to square
                 command=None, # command will execute when button is clicked
                 compound="left", # compound image to left right center top or bottom
                 cursor="hand2", # mouse cursor style
                 default="normal", # default state style
                 dfg="fg-primary", # foreground color when button is disabled
                 font=("Calibri", 9), # font style
                 fg="fg-white", # foreground color
                 height=2, # height of the button instance
                 hlbg="bg-light", # background color when button is highlighted
                 hlc="bg-light", # foreground color when button is highlighted
                 hlt=1, # thickness width when button is highlighted
                 image=None, # image to set in button
                 justify="center", # justify button text left right or center
                 overrelief="groove", # over relief
                 padx=3, # padding in left and right
                 pady=2, # padding in top and bottom
                 relief="flat", # relief
                 rdelay=1000, # repeat delay
                 rinterval=2000, # repeat interval
                 state="normal", # default state normal disable or active
                 takefocus=1, # set button property if button can take focus or not
                 text="Button", # button text value
                 tvar=None, # text variable to set and get dynamic value
                 underline=99, # underline position for text chars
                 width=16, # button width
                 wraplength=0, # text wrap length
                 row=0, # row position
                 column=0, # column position
                 ipadx=0, # inner button padding for left and right
                 ipady=1, # inner button padding for top and bottom
                 hoverbg="bg-warning", # background color when button is hovered
                 hoverfg="fg-dark", # foreground color when button is hovered
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        # image object will be bind into button instance, so it will not be destroy

        self.image = image # set image object to button instance

        # passing all args and kwargs into super tkinter button class

        super(Button, self).__init__(root,
                                     activebackground=color(abg), # color of active background
                                     activeforeground=color(afg), # color of active foreground
                                     anchor=anchor,
                                     bg=color(bg), # color of background
                                     bitmap=bitmap,
                                     bd=bd,
                                     command=command,
                                     compound=compound,
                                     cursor=cursor,
                                     default=default,
                                     disabledforeground=color(dfg), # color of foreground when button is disabled
                                     font=font,
                                     fg=color(fg), # color of foreground
                                     height=height,
                                     highlightbackground=color(hlbg), # color of background when button is highlighted
                                     highlightcolor=color(hlc), # color of foreground when button is highlighted
                                     highlightthickness=hlt,
                                     image=image,
                                     justify=justify,
                                     overrelief=overrelief,
                                     relief=relief,
                                     repeatdelay=rdelay,
                                     repeatinterval=rinterval,
                                     state=state,
                                     takefocus=takefocus,
                                     text=text,
                                     textvariable=tvar,
                                     underline=underline,
                                     width=width,
                                     wraplength=wraplength,
                                     *args, **kwargs
                                )

        # button.grid is called by default
        # so you don't need to call it again
        # you can set row column etc in main class instead

        self.grid(
                row=row,
                column=column,
                padx=padx,
                pady=pady,
                ipadx=ipadx,
                ipady=ipady
            ) # set grid system

        # setting hover effect in button widgets
        # when button will be hovered a background
        # foreground effect will be applied into button

        self.bind("<Enter>", lambda e: self.config(
                                    bg=color(hoverbg), # color background when button is hovered
                                    fg=color(hoverfg)) # color foreground when button is hovered
                                )

        # disable hover effect in button widgets when hover removed
        # when button will be de hovered a background
        # foreground effect will be applied into button by it's previous color

        self.bind("<Leave>", lambda e: self.config(
                                    bg=color(abg) if self['state'] == 'active' else color(bg),
                                    fg=color(afg) if self['state'] == 'active' else color(fg)
                                )
                            )

    def config(self, **kwargs):
        super(Button, self).config(kwargs)

        for key, value in kwargs.items():
            setattr(self, key, value)
