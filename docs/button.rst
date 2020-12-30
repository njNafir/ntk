=======
Button
=======

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to,
good looking and os level implementation.

ntk Button is extended version of tkinter base Button with more functionality and eye touchable design, to use
this Button widget we need to import first it from ntk by

    ``from ntk import Button``

and initialize it by calling it

    ``button1 = Button(root)`` # root is master window, your tkinter window or sub window

call it and see the magic, this will create button and basic grid will be applied, you need to pass parameters described 
below to get your desired button style and grid.

available parameters are:

    * ``root``, # root is a master window to place this button into it
    * ``abg="bg-secondary"``, # background color when button is active
    * ``afg="fg-light"``, # foreground color when button is active
    * ``anchor="center"``, # anchor text to left right or center
    * ``bg="bg-info"``, # background color
    * ``bitmap=None``, # bitmap image to place
    * ``bd=0``, # border width to square
    * ``command=None``, # command will execute when button is clicked
    * ``compound="left"``, # compound image to left right center top or bottom
    * ``cursor="hand2"``, # mouse cursor style
    * ``default="normal"``, # default state style
    * ``dfg="fg-primary"``, # foreground color when button is disabled
    * ``font=("Calibri", 9)``, # font style
    * ``fg="fg-white"``, # foreground color
    * ``height=2``, # height of the button instance
    * ``hlbg="bg-light"``, # background color when button is highlighted
    * ``hlc="bg-light"``, # foreground color when button is highlighted
    * ``hlt=1``, # thickness width when button is highlighted
    * ``image=None``, # image to set in button
    * ``justify="center"``, # justify button text left right or center
    * ``overrelief="groove"``, # over relief
    * ``padx=3``, # padding in left and right
    * ``pady=2``, # padding in top and bottom
    * ``relief="flat"``, # relief
    * ``rdelay=1000``, # repeat delay
    * ``rinterval=2000``, # repeat interval
    * ``state="normal"``, # default state normal disable or active
    * ``takefocus=1``, # set button property if button can take focus or not
    * ``text="Button"``, # button text value
    * ``tvar=None``, # text variable to set and get dynamic value
    * ``underline=99``, # underline position for text chars
    * ``width=16``, # button width
    * ``wraplength=0``, # text wrap length
    * ``row=0``, # row position
    * ``column=0``, # column position
    * ``ipadx=0``, # inner button padding for left and right
    * ``ipady=1``, # inner button padding for top and bottom
    * ``hoverbg="bg-warning"``, # background color when button is hovered
    * ``hoverfg="fg-dark"``, # foreground color when button is hovered

ntk can work with grid manager and it's automated, you just need to pass grid options into Button class
grid options by default set's, so if you don't pass them it will be grided in default row-column setting

an example of creating Button:


    ``from ntk import Tk, Button``

    ``root = Tk(title='Example of ntk window')``

    ``button1 = Button(root, text="click to see effect", row=1, column=1)``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Button class.