# Import Tkinter Entry to use it and modify default

from ntk.widgets.entry import Entry

# Import all util from ntk.utils

from ntk.utils import *

# Import Tkinter Toplevel to use it for list window

from ntk.widgets.toplevel import Toplevel

# Import Tkinter Toplevel to use it for list container

from ntk.widgets.canvas import Canvas


# from ntk.widgets.scroller import Scrollbar
# from ntk.widgets.tk import Tk

# Import gv objects from ntk.objects

from ntk.objects import gv

class SelectBox(Entry):

    # selectbox class can be called for create root tk
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # tk design is custom and can be set twice
    # Tk instance will contain the base tkinter entry instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter entry

    # so if it cause an error most probably it's getting from tkinter entry object
    # see your all arguments and keywords is supporting by ntk Entry or tkinter Entry

    # it contain a values parameter, which can be a list or tuple
    # this values will be rendered as a list which is
    # selectable, scrollable

    # it's hover effect, mouse pointer effect,
    # scroll effect, command effect and more

    # when clicked on entry widget
    # list will be open and appear in a scrollable canvas

    # height can be increased or decreased to fit list height

    # default can be passed to set in entry

    # select command can be passed as a recursive function
    # whenever time list selection happened, this command will be executed

    # onclick is another trick to modify entry
    # when you want to perform a set rule when entry is clicked

    def __init__(self,
                 root, # root is a master window to place this entry into it
                 values=['Values:list/tuple'], # values can be a list or tuple
                 height=10, # height of value list
                 default=True, # default value in entry box
                 selectcommand=False, # to perform when any value is selected
                 bg='#F4F4F4', # background color of select box
                 onclick='', # perform set rule when entry box clicked
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        super(SelectBox, self).__init__(root,
                                        bg=bg,
                                        abg=kwargs.pop('abg', bg), # background color when entry is active,
                                                                        # it will get default or poped if passed
                                        focusinbg=kwargs.pop('focusinbg', bg), # background color when entry is focused,
                                                                        # it will get default or poped if passed
                                        hlbg=kwargs.pop('hlbg', bg), # background color when entry is highlighted,
                                                                        # it will get default or poped if passed
                                        hlc=kwargs.pop('hlc', bg), # foreground color when entry is highlighted,
                                                                        # it will get default or poped if passed
                                        focusinhlc=kwargs.pop('focusinhlc', bg), # foreground color when entry is focused,
                                                                        # it will get default or poped if passed
                                        *args, **kwargs
                                    )

        # set default value for list is False

        self.list = False

        # set object height as passed height
        # so that we can use it from any where in object

        self.height = height

        # set object values as passed values
        # so that we can use it from any where in object

        self.values = self.mvalues = values

        # set object root as passed root
        # so that we can use it from any where in object

        self.root = root

        # set object selectcommand as passed selectcommand
        # so that we can use it from any where in object

        self.selectcommand = selectcommand

        # set object onclick as passed onclick
        # so that we can use it from any where in object

        self.onclick = onclick

        # setattr(gv, str(self) + ':list', False)

        # bind Button Click event to show_selection method
        # because we want to perform show_selection when button clicked

        self.bind("<Button-1>", lambda e: self.show_selection(e))

        # bind Key Release event to typed method
        # because we want to perform typed when key released

        self.bind('<KeyRelease>', lambda e: self.typed(e))

        # check if default is passed, then

        if default:

            # if default is passed,
            # set entry value as default value

            # check if default is just True

            if type(default) == bool:

                # if default is bool and it's True
                # then set default as first item of values list

                default = values[0]

            # next set entry value to default value
            # by entry.set(default)

            self.set(default)


    def show_selection(self, e=None, show=False, values=False):

        # show selection method is used to show all list of values in a window

        # it takes up most three parameters, and these are event, show, values parameters

        # event is used when we want to know event type, event value, keysym etc

        # show can be used for pass an important param as show
        # show is False means list need to be hide
        # and show is True means list need to be open

        # values is used to pass dynamic values list in show_selection

        # if we need to pass custom values list in select box
        # we can pass these by this method and parameters

        # by select.show_selection(event/None, show=True/False, values=list/tuple)

        # check if values passed as list or tuple

        if type(values) != bool:

            # set select.values = passed values

            self.values = self.mvalues = values

        # check if show called

        if show:

            # set select.list_opened = False

            self.list_opened = False

        # check if select.onclick is equal to clean

        if self.onclick == 'clean':

            # check if event is passed

            if e:

                # check if event type is a Button Press

                if e.__dict__['type'].__dict__['_name_'] == 'ButtonPress':

                    # set entry value as empty value
                    # because onclick was clean

                    self.set('')

        elif self.onclick != '':

            # or if select.onclick is not equal to ''
            # then set onclick value to entry value

            self.set(self.onclick)

        # check if not select.list

        if not self.list:

            # if select.list is not defined

            # set rx as select.winfo_rootx

            rx = self.winfo_rootx()

            # set ry as select.winfo_rooty

            ry = self.winfo_rooty()

            # set rw as select.winfo_width

            rw = self.winfo_width()

            # set rh as select.winfo_height

            rh = self.winfo_height()

            # set rx as select object attribute

            self.rx = rx

            # set ry as select object attribute

            self.ry = ry

            # set rw as select object attribute

            self.rw = rw

            # set rh as select object attribute

            self.rh = rh

            # set lv as length of values

            lv = len(self.values)

            # define h = multiplication of rh and preferred height

            h = rh*self.height if lv>self.height else rh*lv

            # define select.list as a list window

            self.list = Toplevel(None,
                                 x=rx, # list window left position
                                 y=ry+rh, # list window bottom position
                                 width=rw, # list window width
                                 height=h, # list window height
                                 bg='bg-white', # list window background color, default is bootstrap referenced white
                                 highlightthickness=1, # thickness width of list window when it's highlighted
                                 highlightbackground=self.focushighlightcolor, # background color of list window
                                                                                    # when list window is highlighted
                                 topbar=False # pass topbar parameter as false, it will not contain top bar
                            )

            # next define main list as list body

            self.list_body = Canvas(self.list, # root window is select.list
                                    width=rw-2, # list window body width
                                    height=h-2, # list window body height
                                    scrollregion=[0,0,rw-15,h-2] # list window body scrolling area
                                )

            # for more control let's set list.protocol WM_DELETE_WINDOW as destroy list

            self.list.protocol("WM_DELETE_WINDOW", self.destroy_list)

            # set select.list.state as withdrawn at first

            self.list.state('withdrawn')

            # list not opened because we set it's state to withdrawn

            self.list_opened = False

            # let's call update list method
            # which is actual function to show our values

            self.update_list()

            # for more control let's set tkinter tk window --
            # Button Click bind to destroy this list

            gv.main_window.bind('<Button-1>', lambda event: self.destroy_list(event))

        elif self.list_opened:

            # else if list is not opened, then
            # set select.list object's state as withdrawn

            self.list.state('withdrawn')

            # as if list is not opened
            # so we need to set list opened as false

            self.list_opened = False

        elif not self.list_opened:

            # else if list is opened, then
            # set select.list state as normal

            self.list.state('normal')

            # as if list opened
            # so we need to set list opened as true

            self.list_opened = True

            # next we can update list again
            # to gain our values list in body

            self.update_list()

    def update_list(self):

        # update list method is used to update values list

        # at first delete all item from values list

        self.list_body.delete('all')

        # set rw as select.winfo_width

        rw = self.winfo_width()

        # set rh as select.winfo_height

        rh = self.winfo_height()

        # let's loop into values list

        for ix, v in enumerate(self.values):

            # check item is current or not
            # if item is equal to entry value then
            # current is True else False

            curr = 0 if v == self.get() else 1

            # set rct as a rectangle of binding single item

            rct = self.list_body.create_rectangle(-2, # x1 position of rectangle
                                                  ix*rh, # y1 position of rectangle,
                                                                # item index multiplied by item height
                                                  rw-2, # x2 position of rectangle
                                                  (ix+1)*rh, # y2 position of rectangle,
                                                                # item index + 1 multiplied by item height
                                                  outline='#FAFAFA', # border color
                                                  fill=['#E9ECEF','white'][curr] # background color
                                            )

            # set txt as a text of binding single item

            txt = self.list_body.create_text(24*(rw/1129), # x position of text
                                             ((ix+1)*rh)-(rh//2), # y position of text,
                                                                # as middle point of item height
                                             fill=['#4c4c4c', '#4c4c4c'][curr], # text color
                                             font=self['font'], # font style
                                             text=str(v), # text
                                             anchor="w" # anchor text to w e we s n se ne etc
                                        )

            # bind rectangle Enter event by values list body to mouse entered

            self.list_body.tag_bind(rct, '<Enter>', lambda e, r=rct, t=txt: self.mouse_entered(r, t))

            # bind rectangle Leave event by values list body to mouse leaved

            self.list_body.tag_bind(rct, '<Leave>', lambda e, r=rct, t=txt: self.mouse_leaved(r, t))

            # bind rectangle Button Click event by values list body to select text

            self.list_body.tag_bind(rct, '<Button-1>', lambda e, t=str(v): self.select_text(t))

            # bind rectangle Button Click event by values list body to select text

            self.list_body.tag_bind(rct, '<Button-1>', lambda e, t=str(v): self.select_text(t))

            # bind text Enter event by values list body to mouse entered

            self.list_body.tag_bind(txt, '<Enter>', lambda e, r=rct, t=txt: self.mouse_entered(r, t))

            # bind text Leave event by values list body to mouse leaved

            self.list_body.tag_bind(txt, '<Leave>', lambda e, r=rct, t=txt: self.mouse_leaved(r, t))

            # bind text Button Click event by values list body to select text

            self.list_body.tag_bind(txt, '<Button-1>', lambda e, t=str(v): self.select_text(t))

            # bind text Button Click event by values list body to select text

            self.list_body.tag_bind(txt, '<Button-1>', lambda e, t=str(v): self.select_text(t))

            # configure select.list_body scroll region to new width height

            self.list_body.config(
                            scrollregion=[
                                0, # x1 position for scroll region
                                0, # y1 position for scroll region
                                rw-15, # x2 position for scroll region
                                (ix+1)*rh # y2 position for scroll region
                            ]
                    )

    def mouse_entered(self, ir, it):

        # this method will be called when select.mouse_entered executed

        # when mouse entered, let's update list item rectangle background to hovered color

        self.list_body.itemconfig(ir, fill="#E9ECEF")

        # when mouse entered, let's update list item text background to hovered color

        self.list_body.itemconfig(it, fill="#4c4c4c")

        # when mouse entered, let's update list body cursor object to hand2

        self.list_body.config(cursor="hand2")

    def mouse_leaved(self, ir, it):

        # this method will be called when select.mouse_leaved executed

        # when mouse leaved, let's update list item rectangle background to previous color

        self.list_body.itemconfig(ir, fill="white")

        # when mouse leaved, let's update list item text background to previous color

        self.list_body.itemconfig(it, fill="#4c4c4c")

        # when mouse leaved, let's update list body cursor object to arrow again

        self.list_body.config(cursor="arrow")

    def select_text(self, t):

        # this method will be called when select.select_text executed

        # at first set entry value as selected item text

        self.set(t)

        # destroy and delete list window from root window

        self.list.destroy()

        # set select.list as False

        self.list = False

        # check if select command is passed
        # if it passed, then execute it by calling it

        if self.selectcommand:

            # let's call the select command function

            self.selectcommand()

    def typed(self, e):

        # this method will be called when select.typed executed

        # at first get the current value of entry

        tx = self.get()

        # define default value of new_values as empty list

        new_values = []

        # loop over all values to get and set

        for el in self.mvalues:

            # check if searched text is matching with this item

            if tx in el:

                # if searched value is matching with list item
                # add this item to new values list

                new_values.append(el)

        # check if new values list is empty

        if not new_values:

            # if new values list is empty
            # then append a new value as 'No result found' in the new values list

            new_values.append('No result found')

        # next set select.values as new values

        self.values = new_values

        # check if select.list type is bool

        if type(self.list) != bool:

            # if select.list type is bool, then
            # destroy select.list window

            self.list.destroy()

            # set select.list as false

            self.list = False

        # let's recall select.show_selection to reset
        # list with new  values

        self.show_selection(e)

        # let's recall select.show_selection twice to show up list
        # list with new  values

        self.show_selection(e)

    def destroy_list(self, e):

        # destroy list method is used to destroy full list and window

        # set ex as event.x_root

        ex = e.x_root

        # set ey as event.y_root

        ey = e.y_root

        # let's execute a complex check and understand
        # the important and problem of destroying the list and list window

        if type(self.list) != bool and not (ex>self.rx and ex<(self.rx + self.rw) and \
            ey>self.ry and ey<(self.ry + self.rh)):

            # if everything is okay, let's destroy list and list window

            self.list.destroy()

            # as we destroyed our list, we can now set select.list as False

            self.list = False
