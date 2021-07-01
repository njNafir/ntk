# Import Tcl Tkinter Combobox to use it and modify default

from tkinter.ttk import Combobox as ttkCombobox

class Combobox(ttkCombobox):

    # combobox class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # every design is custom and can be set twice
    # Combobox instance will contain the base tcl tkinter combobox instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter combobox

    # so if it cause an error most probably it's getting from tkinter combobox object
    # see your all arguments and keywords is supporting by ntk Combobox or tkinter combobox

    def __init__(self,
                 root, # root is a master window to place this combobox into it
                 class_="TCombobox", # combobox class which can be inherited
                 cursor="arrow", # cursor style when mouse over combobox
                 exportselection=1, # copy selected text when selection appeared in combobox
                 height=24, # height of value list
                 justify="left", # justify combobox text left right or center
                 postcommand="", # combobox postcommand when selected item
                 style="TCombobox", # combobox style object
                 takefocus=1, # set take focus to 0 if you don't want to focusing effect
                 textvariable=False, # combobox text variable, to get and set value dynamically
                 validate=None, # validate
                 validatecommand=False, # validate command
                 values=['No more item'], # combo values to set as a list
                 width=24, # combobox width
                 xscrollcommand=False, # combobox left right scrolling
                 font=("Calibri", 10), # combobox font style
                 row=0, # row position
                 column=0, # column position
                 padx=0, # padding for left and right
                 pady=0, # padding for top and bottom
                 ipady=2, # internal padding for top and bottom
                 sticky='w', # combobox sticky position w, e, s, n, we, ne, se etc
                 text="-----", # default text in combobox widget
                 default=0, # default text index from value list
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        # values by default text and values list merge

        values = [text] + list(values)

        # return into super class
        # and pass every arguments and keywords
        # into that class

        super(Combobox, self).__init__(root,
                                       class_=class_,
                                       cursor=cursor,
                                       exportselection=exportselection,
                                       height=height,
                                       justify=justify,
                                       postcommand=postcommand,
                                       validate=validate,
                                       validatecommand=validatecommand,
                                       style=style,
                                       takefocus=takefocus,
                                       textvariable=textvariable,
                                       values=values,
                                       width=width,
                                       xscrollcommand=xscrollcommand,
                                       font=font,
                                       *args, **kwargs
                                )

        # combobox.grid command to adding widget in root window

        self.grid(
                row=row, # grid row position
                column=column, # grid column position
                padx=padx, # grid padding left and right
                pady=pady, # grid padding top and bottom
                ipady=ipady, # grid internal padding top and bottom
                sticky=sticky # grid sticky position
            )

        # set default value in combobox

        # this default value is getting from values list
        # and default=index keyword is passed in combobox class

        # when we get this index
        # we are trying to get this index from values list
        # and setting in to combobox

        # if requested index is not parsable from list if will
        # cause an error

        self.set(values[default])
