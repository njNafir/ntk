========
Notebook
========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Notebook is multi window wrapper for ntk window, we can create a notebook and add tabs for getting multi window in tabs

ntk Notebook is extended version of tkinter ttk/tcl-tk base Notebook with more functionality and responsive grid system, to use
this Notebook window we need to import first it from ntk by

    ``from ntk import Notebook``

and initialize it by calling it

    ``window = Notebook(root)``

This will create wrapper and basic style will be applied, you need to pass parameters described 
below to get your desired window size and style

available parameters are:

    * ``root``, # root is a master window to place this notebook into it
    * ``class_="TNotebook"``, # notebook class to inherit object
    * ``cursor="arrow"``, # cursor style for notebook window
    * ``height=180``, # notebook height
    * ``width=350``, # notebook width
    * ``takefocus=0``, # set notebook window can take focus or not
    * ``padding=0``, # padding in square window
    * ``bg="bg-light"``, # background color, default is bootstrap referenced light
    * ``bd=0``, # border width
    * ``fg="fg-dark"``, # foreground color, default is bootstrap referenced dark
    * ``lightcolor="fg-info``", # light color, default is bootstrap referenced info
    * ``row=0``, # grid row position
    * ``column=0``, # grid column position
    * ``sticky="wn"``, # grid sticky position
    * ``rowspan=1``, # grid row span width
    * ``columnspan=1``, # grid column span width
    * ``padx=1``, # grid padding left and right
    * ``pady=1``, # grid padding top and bottom
    * ``style=False``, # notebook default style

an example of creating Notebook window:


    ``from ntk import Tk, Notebook, PanedWindow``

    ``root = Tk(title='Example of ntk window')``

    ``notebook = Notebook(root)``

    ``root.mainloop()``

Notebook wrapper has a method called add, which can be used for adding a tab in Notebook
for doing this,

    ``panedwindow = PanedWindow(notebook)`` # create a panedwindow to add it into NoteBook

    ``notebook.add(child=panedwindow, text='First tab')``

we can pass other parameters to add method, and those are,

    * ``width=16``, # tab head title width/text width
    * ``image=False``, # not supported yet
    * ``compound="left"``, # can be used for image
    * ``underline=99``, # underline position for tab header text
    * ``sticky="wn``", # sticky position
    * ``padding=0`` # padding

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Notebook class.