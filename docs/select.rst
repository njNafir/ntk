=========
SelectBox
=========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

SelectBox is a box widget, where we can show up a list of possible options, 
we can scroll on it and we can bind events for advance handling

ntk SelectBox is merged version of ntk Entry, Toplevel and Canvas, 
with more functionality, responsive grid system and with automation, to use
this SelectBox window we need to import first it from ntk by

    ``from ntk import SelectBox``

and initialize it by calling it

    ``SelectBox = SelectBox(root)``

This will create a SelectBox in given grid and basic style will be applied, 
you need to pass parameters described below

available parameters are:

    * root, # root is a master window to place this entry into it
    * values=['Values:list/tuple'], # values can be a list or tuple
    * height=10, # height of value list
    * default=True, # default value in entry box
    * selectcommand=False, # to perform when any value is selected
    * bg='#F4F4F4', # background color of select box
    * onclick='', # perform set rule when entry box clicked

an example of creating SelectBox widget:


    ``from ntk import Tk, SelectBox``

    ``root = Tk(title='Example of ntk window')``

    ``select = SelectBox(root, values=['First', 'Second', 'Third'])``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to ntk Entry class.

SelectBox class have other custom method, which can be used to handle SelectBox widget

SelectBox.show_selection() method is can be used to pop up the list of selection options in Once

    ``select.show_selection()``

it has passable three parameters

    * e=None, # event object
    * show=False, # list show or hide
    * values=False # pass value list another time

SelectBox.update_list() method is can be used to reset list of values from box

    ``select.update_list()``

SelectBox.mouse_entered() method is used by SelectBox object itself to set option hover style

    ``select.mouse_entered(1, 2)``

SelectBox.mouse_leaved() method is used by SelectBox object itself to set option hover removed style

    ``select.mouse_leaved(1, 2)``

SelectBox.select_text() method is used by SelectBox object itself to select text and call selectcommand

    ``select.select_text("Third")``

SelectBox.typed() method is used by SelectBox object itself bind method when key pressed in entry

    ``select.typed(e)`` # e is event object

SelectBox.destroy_list() method is used by SelectBox object itself bind method when we want to destroy the list

    ``select.destroy_list(e)`` # e is event object
