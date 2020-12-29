========
Toplevel
========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Toplevel is window like Tk window, but it has no mainloop method so it can be used for sub window

ntk Toplevel is extended version of tkinter base Toplevel with more functionality and responsive grid system, to use
this Toplevel window we need to import first it from ntk by

    from ntk import Toplevel

and initialize it by calling it

    window = Toplevel(root)

This will create window and basic style will be applied, you need to pass parameters described 
below to get your desired window size and style

available parameters are:

* root=None, # root is a master window to place this toplevel into it
* title="Toplevel", # title to showing on top bar
* bg="bg-white", # background color, default is bootstrap referenced white
* bd=0, # border width
* class_="Toplevel", # class is important when you want to inherit any design or some methods
* colormap=False, # color map
* container=0, # container
* cursor="arrow", # cursor style for toplevel
* height=480, # toplevel window height
* width=360, # toplevel window width
* highlightbackground="bg-light", # background color when toplevel is highlighted default is bootstrap referenced light
* highlightcolor="fg-dark", # foreground color when toplevel is highlighted default is bootstrap referenced dark
* highlightthickness=0, # thickness width of toplevel when highlighted
* menu=False, # top level menu can be set with this command
* padx=0, # grid padding left and right
* pady=0, # grid padding top and bottom
* relief="flat", # toplevel relief style
* screen="", # toplevel screen
* takefocus=1, # set if toplevel window can take focus or not
* use=False, # use
* visual=False, # visual
* resize_x=0, # toplevel window resizing horizontally is allowed or not
* resize_y=0, # toplevel window resizing vertically is allowed or not
* x=False, # toplevel window positioning left right position
* y=False, # toplevel window positioning top bottom position
* topbar=True

an example of creating Toplevel window:


    from ntk import Tk, Toplevel

    root = Tk(title='Example of ntk window')

    sub_window = Toplevel(root, title='Example of sub window')

    root.mainloop()

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Toplevel class.