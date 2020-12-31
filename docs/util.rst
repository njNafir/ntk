=======
Utils
=======

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to,
good looking and os level implementation.

ntk Utils are some functions which can be used to get some powerfull options in our program

    ``from ntk.utils import *``

    ``bg_colors = bg_colors()``

it will return ntk supported background colors referenced to bootstrap

    ``fg_colors = fg_colors()``
    
it will return ntk supported background colors referenced to bootstrap

    ``white = color("#FFFFFF")``
    
it will return absolute color value for given param, by matching query from foreground, background and actual

    ``delete_child(master)``
    
delete_child function will destroy all child widget from any widget which is passed as a master

exclude param can be used to exclude any single type, like

    ``delete_child(master, exclude='label')`` # it will delete all child widget except label widget

just param can be used to delete any single type, like

    ``delete_child(master, just='label')`` # it will delete all child widget which is a label widget

another useful utils is w and h, this two utils can be used to get dynamic and responsive width and height 
for given width or height

    ``width = w(500)`` 
    
it will return responsive 500 width, it can be smaller or bigger number with respect to device width

    ``height = h(620)`` 

it will return responsive 500 height, it can be smaller or bigger number with respect to device height

w and h function also can be imported and used by gv (global var) object, we will
talk about gv in the objects.gv page