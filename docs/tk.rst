=======
Tk
=======

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to,
good looking and os level implementation.

ntk Tk is extended version of tkinter base Tk with more functionality and responsive grid system, to use
this Tk window we need to import first it from ntk by

    from ntk import Tk

and initialize it by calling it

    root = Tk()
    root.mainloop()

This will create tk window and basic grid will be applied, you need to pass parameters described 
below to get your desired window size, style and grid.

available parameters are:

* title="Main Window", # title to showing on top bar
* resize_x=True, # resize x is to set horizontal resizable
* resize_y=True, # resize y is to set vertical resizable
* width=360, # tkinter window width
* height=380, # tkinter window height
* x=False, # tkinter window positioning root x
* y=False, # tkinter window positioning root y
* state="normal", # tkinter window state
* bg="bg-white", # background of tkinter window, default is bootstrap referenced white
* icon=False, # tkinter window icon
* mainframe=True, # set if tkinter hold a main frame window or not
* fullscreen=False, # set if you want to set this window to full window
* gridrow=1, # grid configure row position
* gridcolumn=1, # grid configure column position
* topbar=True

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Tk class.