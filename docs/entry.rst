========
Entry
========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Entry is a box widget in ntk where we can write anything, and 
it has more functionality to get and set value, binding events etc

ntk Entry is extended version of tkinter base Entry, 
with more functionality, responsive grid system and with automation, to use
this Entry window we need to import first it from ntk by

    ``from ntk import Entry``

and initialize it by calling it

    ``entry = Entry(root)``

This will create a entry in given grid and basic style will be applied, you need to pass parameters described 
below to get your desired window size and style

available parameters are:

    * ``root``, # root is a master window to place this entry into it
    * ``bg="bg-light"``, # background color, default is bootstrap referenced light
    * ``bd=0``, # border width of entry widget
    * ``cursor="xterm``", # default cursor style
    * ``dbg="bg-warning"``, # background color when entry is disabled, default is bootstrap referenced warning
    * ``dfg="fg-dark"``, # foreground color when entry is disabled, default is bootstrap referenced dark
    * ``eselect=1``, # when entry text is selected it will automatically exported to clipboard
    * ``font=("Calibri", 11)``, # font styles
    * ``fg="fg-secondary"``, # foreground color, default is bootstrap referenced secondary
    * ``hlbg="bg-primary"``, # background color when entry is highlighted, default is bootstrap referenced primary
    * ``hlc="fg-primary"``, # foreground color when entry is highlighted, default is bootstrap referenced primary
    * ``hlt=1``, # thickness width when entry is highlighted
    * ``ibg="bg-dark"``, # background color for inserted char, default is bootstrap referenced dark
    * ``ibd=0``, # border width for inserted char
    * ``iofftime=500``, # insert off time for shuffling insert bar
    * ``iontime=500``, # insert on time for shuffling insert bar
    * ``iwidth=2``, # insert bar width
    * ``invcmd=""``, # inv cmd line
    * ``justify="left"``, # entry text justify left right center
    * ``rbg="bg-white"``, # background color when entry is readonly, default is bootstrap referenced white
    * ``relief="flat"``, # entry relief style flat groove etc
    * ``sbg="bg-primary"``, # entry selection background, default is bootstrap referenced primary
    * ``sbd=2``, # border width of selection text
    * ``sfg="fg-white"``, # entry selection foreground, default is bootstrap referenced white
    * ``show=None``, # show is to define text visual, if you set it to * all text chars will be visible as * but it's main value original
    * ``state="normal"``, # entry state normal disable readonly etc
    * ``takefocus=1``, # set entry widget can take focus or not
    * ``tvar=None``, # text variable for entry to get and set value dynamically
    * ``validate=None``, # validate
    * ``vcmd=None``, # vc md
    * ``width=24``, # entry width
    * ``xscrollcommand=None``, # scrolling command when scrolling in left-right position
    * ``row=0``, # grid row position
    * ``column=0``, # grid column position
    * ``columnspan=1``, # grid column span position
    * ``rowspan=1``, # grid row span position
    * ``padx=10``, # grid padding left and right
    * ``pady=10``, # grid padding top and bottom
    * ``ipady=2``, # grid internal padding top and bottom
    * ``sticky='w'``, # grid sticky position
    * ``default=""``, # entry widget default value
    * ``focusinbg="bg-white"``, # background color when entry is focused, default is bootstrap referenced white
    * ``focusoutbg=False``, # background color when entry is unfocused, default is False means it will set main bg again
    * ``focusinhlc="bg-warning"``, # foreground color when entry is focused, default is bootstrap referenced warning
    * ``focusouthlc=False``, # foreground color when entry is unfocused, default is False means it will set main bg again

an example of creating Entry widget:


    ``from ntk import Tk, Entry``

    ``root = Tk(title='Example of ntk window')``

    ``entry = Entry(root)``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Entry class.

Entry has another method called set, and set method can be used for setting text value in it. like this

    ``entry.set("New value")``