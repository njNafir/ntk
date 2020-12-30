========
Frame
========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Frame is multi widget wrapper for ntk window, we can create a frame 
and separate sub widgets in main window by combining into frames

ntk Frame is extended version of tkinter base Frame with more functionality and responsive grid system, to use
this Frame window we need to import first it from ntk by

    ``from ntk import Frame``

and initialize it by calling it

    ``window = Frame(root)``

This will create wrapper and basic style will be applied, you need to pass parameters described 
below to get your desired window size and style

available parameters are:

    * ``root``, # root is a master window to place this frame into it
    * ``bg="bg-white"``, # background color, default is bootstrap referenced white
    * ``bd=0``, # border width
    * ``colormap=None``, # color map
    * ``class_=False``, # class name to inherit styles and methods
    * ``container=0``, # container
    * ``cursor="arrow"``, # mouse cursor style arrow hand2 etc
    * ``height=64``, # frame height
    * ``highlightbackground="bg-light"``, # background color when frame is highlighted, default is bootstrap referenced light
    * ``highlightcolor="bg-dark"``, # foreground color when frame is highlighted, default is bootstrap referenced dark
    * ``highlightthickness=0``, # thickness width when frame is highlighted
    * ``row=0``, # grid row position
    * ``column=0``, # grid column position
    * ``padx=0``, # grid padding left and right
    * ``pady=0``, # grid padding top and bottom
    * ``relief="flat"``, # relief style flat groove etc
    * ``sticky="w"``, # grid sticky position
    * ``takefocus=0``, # set frame can take focus or not
    * ``visual=0``, # visual
    * ``width=128``, # frame width
    * ``gridrow=1``, # grid row configure row weight
    * ``gridcolumn=1``, # grid column configure column weight

an example of creating Frame widget:


    ``from ntk import Tk, Frame``

    ``root = Tk(title='Example of ntk window')``

    ``frame = Frame(root)``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Frame class.