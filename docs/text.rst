=========
Text
=========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Text is a box widget, where we can type text in multi line, 
we can scroll on it and we can bind events for advance handling

ntk Text is extended version of tkinter base Text, 
with more functionality, responsive grid system and with automation, to use
this Text window we need to import first it from ntk by

    ``from ntk import Text``

and initialize it by calling it

    ``Text = Text(root)``

This will create a Text in given grid and basic style will be applied, 
you need to pass parameters described below

available parameters are:

    * root, # root is a master window to place this text into it
    * sep=1, # auto separator
    * bg="bg-light", # background of text widget, default is bootstrap referenced light
    * bd=0, # border width
    * cursor="xterm", # cursor style to showing in insert position
    * eselection=1, # export selection to clipboard when text is selected
    * font=("Calibri", 10), # font style
    * fg="fg-dark", # foreground of text widget, default is bootstrap referenced dark
    * height=12, # height of text widget
    * hlbg="bg-light", # background when text widget is highlighted, default is bootstrap referenced light
    * hlc="bg-light", # foreground when text widget is highlighted, default is bootstrap referenced light
    * hlt=1, # thickness width of text when it's highlighted
    * ibg="bg-light", # background of inserted position, default is bootstrap referenced light
    * ibd=0, # insert position border width
    * iofftime=500, # insert off time for text widget
    * iontime=1000, # insert on time for text widget
    * iwidth=1, # insert position width
    * maxundo=1, # max undo with control z
    * padx=5, # grid padding left and right
    * pady=5, # grid padding top and bottom
    * relief="flat", # relief style for text widget
    * sbg="bg-primary", # background color of select background, default is bootstrap referenced primary
    * sbd=0, # select border width
    * sfg="fg-white", # foreground color of select background, default is bootstrap referenced primary
    * setgrid=0, # set grid
    * spacing1=0, # first spacing
    * spacing2=0, # second spacing
    * spacing3=0, # third spacing
    * state="normal", # text widget state
    * tabs=None, # text widget tabs
    * takefocus=1, # set if text widget can take focus or not
    * undo=1, # set undo length
    * width=48, # text widget width
    * wrap="char", # text widget wrapping method char or word
    * xscroll=None, # horizontal scroll
    * yscroll=None, # vertical scroll
    * row=0, # grid row position
    * column=0, # grid column position
    * columnspan=1, # grid column span
    * rowspan=1, # grid row span
    * sticky="w", # grid sticky position
    * tvar=False, # text variable for dynamic get and set

an example of creating Text widget:


    ``from ntk import Tk, Text``

    ``root = Tk(title='Example of ntk window')``

    ``text = Text(root)``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Text class.

Text class have other custom method, which can be used to handle text widget

text.clear() method is can be used to clear all text from this text widget

    ``text.clear()``

text.get() method is can be used to get text widget value 

    ``text.get()``

text.set() method is can be used to set text widget value 

    ``text.set("New value")``