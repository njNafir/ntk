========
Combobox
========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Combobox is a box widget in ntk where we can show up selection list

ntk Combobox is extended version of tkinter base Combobox, 
with more functionality, responsive grid system and with automation, to use
this Combobox window we need to import first it from ntk by

    ``from ntk import Combobox``

and initialize it by calling it

    ``Combobox = Combobox(root)``

This will create a Combobox in given grid and basic style will be applied, you need to pass parameters described 
below to get your desired window size and style

available parameters are:

    * root, # root is a master window to place this combobox into it
    * class_="TCombobox", # combobox class which can be inherited
    * cursor="arrow", # cursor style when mouse over combobox
    * exportselection=1, # copy selected text when selection appeared in combobox
    * height=24, # height of value list
    * justify="left", # justify combobox text left right or center
    * postcommand="", # combobox postcommand when selected item
    * style="TCombobox", # combobox style object
    * takefocus=1, # set take focus to 0 if you don't want to focusing effect
    * textvariable=False, # combobox text variable, to get and set value dynamically
    * validate=None, # validate
    * validatecommand=False, # validate command
    * values=['No more item'], # combo values to set as a list
    * width=24, # combobox width
    * xscrollcommand=False, # combobox left right scrolling
    * font=("Calibri", 10), # combobox font style
    * row=0, # row position
    * column=0, # column position
    * padx=0, # padding for left and right
    * pady=0, # padding for top and bottom
    * ipady=2, # internal padding for top and bottom
    * sticky='w', # combobox sticky position w, e, s, n, we, ne, se etc
    * text="-----", # default text in combobox widget
    * default=0, # default text index from value list

an example of creating Combobox widget:


    ``from ntk import Tk, Combobox``

    ``root = Tk(title='Example of ntk window')``

    ``Combobox = Combobox(root)``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Combobox class.