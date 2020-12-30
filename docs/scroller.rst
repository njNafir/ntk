========
Scroller
========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Scrollbar is scroll maintaining widget in ntk, 
we can create a scroller widget to set it with other master window like canvas

ntk Scrollbar is extended version of tkinter base Scrollbar, 
with more functionality, responsive grid system and with automation, to use
this Scrollbar window we need to import first it from ntk by

    ``from ntk import Scrollbar``

and initialize it by calling it

    ``scroller = Scrollbar(root)``

This will create a scroller in given orient and basic style will be applied, you need to pass parameters described 
below to get your desired window size and style

available parameters are:

    * ``root``, # root is a master window to place this scrollbar into it
    * ``scroll_on=False``, # set scroll on window/widget, set scroll effect on this window
    * ``orient="vertical"``, # scroll orient left-right or top-bottom
    * ``width=12``, # scrollbar width
    * ``row=0``, # grid row position
    * ``column=1``, # grid column position
    * ``columnspan=1``, # grid column span
    * ``padx=0``, # grid padding left and right
    * ``pady=0``, # grid padding top and bottom
    * ``sticky="ns"``, # grid sticky position
    * ``activebg="bg-light"``, # background color when scrollbar is active, default is bootstrap referenced light
    * ``activerelief="flat"``, # relief style when scrollbar is active
    * ``bg="bg-dark"``, # background color, default is bootstrap referenced dark
    * ``bd=0``, # border width
    * ``cursor="arrow"``, # cursor style for scrollbar
    * ``elementborderwidth=0``, # element border width
    * ``highlightbg="bg-primary"``, # background color when bar is highlighted, default is bootstrap ref primary
    * ``highlightcolor="fg-dark"``, # foreground color when bar is highlighted, default is bootstrap ref dark
    * ``highlightthickness=1``, # bar thickness width when bar is highlighted
    * ``jump=True``, # jump scrolling when clicked on bar
    * ``relief="flat"``, # relief style for bar
    * ``repeatdelay=300``, # bar repeat delay
    * ``repeatinterval=100``, # bar repeat interval
    * ``takefocus=1``, # set if bar can take focus or not
    * ``troughcolor="fg-secondary"``, # bar trough color, default is bootstrap referenced secondary
    * ``gridrow=1``, # grid configure row weight
    * ``gridcolumn=1``, # grid configure column weight

an example of creating Scrollbar widget:


    ``from ntk import Tk, Scrollbar, Canvas``

    ``root = Tk(title='Example of ntk window')``

    ``canvas = Canvas(root)``

    ``scroller = Scrollbar(root, scroll_on=canvas)``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Scrollbar class.