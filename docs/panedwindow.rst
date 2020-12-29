===========
Panedwindow
===========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

PanedWindow is widget wrapper for ntk window, it's highly responsible, it can give us resizable box layout

ntk PanedWindow is extended version of tkinter base PanedWindow with more functionality and responsive grid system, to use
this PanedWindow window we need to import first it from ntk by

    from ntk import PanedWindow

and initialize it by calling it

    paned_window = PanedWindow(root)

This will create window and basic style will be applied, you need to pass parameters described 
below to get your desired window size and style

available parameters are:

* root, # root is a master window to place this panedwindow into it
* bg="bg-light", # background color, default is bootstrap referenced light
* bd=2, # border width
* cursor="arrow", # cursor style for paned window
* handlepad=0, # panedwindow subwidgets handling bar, this also work as bar width
* handlesize=0, # panedwindow subwidgets handling bar, this also work as bar width
* height=370, # panedwindow height
* opaqueresize=0, # opaque resize
* orient="vertical", # panedwindow subwidgets orientation
* relief="flat", # panedwindow relief style flat groove etc
* sashcursor="sizing", # panedwindow subwidgets handling sash bar cursor
* sashpad=0, # panedwindow subwidgets handling sash bar show or hide
* sashrelief="flat", # panedwindow subwidgets handling sash bar relief
* sashwidth=4, # panedwindow subwidgets handling sash bar width
* showhandle=True, # sash handle with handle pad
* width=370, # panedwindow width
* row=0, # grid row position
* column=0, # grid column position
* rowspan=1, # grid row span width
* columnspan=1, # grid column span width
* padx=(0, 0), # grid padding left and right
* pady=(0, 0), # grid padding top and bottom
* ipady=0, # grid internal padding top and bottom
* sticky="wsen", # grid sticky position
* gridrow=1, # grid configure row config weight
* gridcolumn=1, # grid configure column config weight

ntk Tk window already contain a PanedWindow object by default because we passed mainframe=True
we can access it by root.mainframe

an example of creating PanedWindow window:


    from ntk import Tk, PanedWindow

    root = Tk(title='Example of PanedWindow in ntk window')

    paned_window = PanedWindow(root)

    root.mainloop()

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter PanedWindow class.