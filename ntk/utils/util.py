# Import global variable object

from ntk.objects import gv
from datetime import datetime

# BG Colors to set higher level color scheme for UI Interface
# Every color can be set by their unique name

def bg_colors():

    # This color scheme referenced from bootstap color scheme
    # So it's highly recommended color scheme for UI

    # Calling this function will return this dictionary object as all supported color scheme
    # It can be imported from ntk.utils import bg_colors

    # This only contain background colors so It recommend to use this color to background coloring

    return {
        "bg-primary": "#007BFF",
        "bg-secondary": "#6C757D",
        "bg-success": "#28A745",
        "bg-danger": "#DC3545",
        "bg-warning": "#FFC107",
        "bg-info": "#17A2B8",
        "bg-light": "#F8F9FA",
        "bg-dark": "#343A40",
        "bg-white": "#FFFFFF"
    }

def fg_colors():

    # This color scheme referenced from bootstap color scheme
    # So it's highly recommended color scheme for UI

    # Calling this function will return this dictionary object as all supported color scheme
    # It can be imported from ntk.utils import fg_colors

    # This only contain foreground colors so It recommend to use this color to foreground coloring

    return {
        "fg-primary": "#007BFF",
        "fg-secondary": "#6C757D",
        "fg-success": "#28A745",
        "fg-danger": "#DC3545",
        "fg-warning": "#FFC107",
        "fg-info": "#17A2B8",
        "fg-light": "#F8F9FA",
        "fg-dark": "#343A40",
        "fg-white": "#FFFFFF"
    }

def color(name):

    # color util is most used custom util in ntk
    # this util will take a color name or alias

    # if it is matching with any of foreground or background color name
    # it will return that color query by the name

    # if it is not matching with any color name provided in fg_colors and bg_colors
    # it will return that name only

    # so it's a dynamic coloring, you can test any name in color() function if you
    # are to find that color in default color set it will return your color

    # check if color name found in background color list
    if name in bg_colors():
        # executed when name is in background colors

        # return the color code that matched
        return bg_colors()[name]

    # check if color name found in foreground color list
    elif name in fg_colors():
        # executed when name is in foreground colors

        # return the color code that matched
        return fg_colors()[name]

    else:
        # executed when name is not in foreground colors and not in background color

        # return the name
        return name


def delete_child(master, exclude=False, just=False):

    # delete child util is most used util for deleting and destroying any widget and it's subwidgets
    # when you call to delete_child(widget_obj)
    # it will delete all subwidgets and widget itself to withdraw permanently it from your window

    # it have three parameter

    # master is widget object

    # exclude is widget type name, if it passed function will check for it to exclude this type widgets when
    # deleting all widget recursively

    # just is widget type name, if it passed function will check for it to delete this type widgets when
    # deleting all widget recursively


    # get all subwidgets from this widget

    children = master.children

    # check if exclude object is got
    if exclude:

        # if exclude is got, program will exclude this type of widget to delete when deleting all subwidget recursively

        # get all subwidget in a dictionary to iterate and delete after setup

        # add name and value object to children dictionary
        # iterate over all children
        # check if name is matching with exclude name or not

        children = dict((k, v) \
                        for k,v in children.items() \
                        if not k.startswith("!%s" %exclude.lower()))

    if just:
        # if just is got, program will include just this type of widget to delete
        # when deleting all subwidget recursively

        # get all subwidget in a dictionary to iterate and delete after setup

        # add name and value object to children dictionary
        # iterate over all children
        # check if name is matching with just object type or not

        children = dict((k, v) \
                        for k,v in children.items() \
                        if k.startswith("!%s" %just.lower()))

    for k, child in children.items():

        # now iterate over all children to get single item at a item and destroy it

        # object.destroy() will delete it and withdraw it from the window

        child.destroy()

def w(w=0.1):

    # function w is a way of getting responsive width

    # when you passing a width integer it will back you a possible responsive width

    return int(w*gv.wpc)

def h(h=0.1):

    # function h is a way of getting responsive height

    # when you passing a height integer it will back you a possible responsive height

    return int(h*gv.hpc)


def error_log(error="Log file", filename="logs.txt"):
    with open(filename, 'a+') as f:
        f.write(str(datetime.now()) + " --> " + error + '\n')


# add w widget in global var object,
# so it can be used from anywhere
# where global var object gv is available

gv.w    = w

# add h widget in global var object,
# so it can be used from anywhere
# where global var object gv is available
gv.h    = h

gv.error_log = error_log
