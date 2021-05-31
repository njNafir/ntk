# Import Tkinter Entry to use it and modify default

from tkinter import Entry as tkEntry

# Import all util from ntk.utils

from ntk.utils import *

class Entry(tkEntry):

    # entry class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # every design is custom and can be set twice
    # Entry instance will contain the base tkinter entry instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter entry

    # so if it cause an error most probably it's getting from tkinter entry object
    # see your all arguments and keywords is supporting by Entry or tkinter entry

    def __init__(self,
                 root, # root is a master window to place this entry into it
                 bg="bg-light", # background color, default is bootstrap referenced light
                 bd=0, # border width of entry widget
                 cursor="xterm", # default cursor style
                 dbg="bg-warning", # background color when entry is disabled, default is bootstrap referenced warning
                 dfg="fg-dark", # foreground color when entry is disabled, default is bootstrap referenced dark
                 eselect=1, # when entry text is selected it will automatically exported to clipboard
                 font=("Calibri", 11), # font styles
                 fg="fg-secondary", # foreground color, default is bootstrap referenced secondary
                 hlbg="bg-primary", # background color when entry is highlighted,
                                                        # default is bootstrap referenced primary
                 hlc="fg-primary", # foreground color when entry is highlighted,
                                                        # default is bootstrap referenced primary
                 hlt=1, # thickness width when entry is highlighted
                 ibg="bg-dark", # background color for inserted char,
                                                        # default is bootstrap referenced dark
                 ibd=0, # border width for inserted char
                 iofftime=500, # insert off time for shuffling insert bar
                 iontime=500, # insert on time for shuffling insert bar
                 iwidth=2, # insert bar width
                 invcmd="", # inv cmd line
                 justify="left", # entry text justify left right center
                 rbg="bg-white", # background color when entry is readonly,
                                                        # default is bootstrap referenced white
                 relief="flat", # entry relief style flat groove etc
                 sbg="bg-primary", # entry selection background,
                                                        # default is bootstrap referenced primary
                 sbd=2, # border width of selection text
                 sfg="fg-white", # entry selection foreground,
                                                        # default is bootstrap referenced white
                 show=None, # show is to define text visual, if you set it to * all text chars will be visible as * but
                                                        # it's main value original
                 state="normal", # entry state normal disable readonly etc
                 takefocus=1, # set entry widget can take focus or not
                 tvar=None, # text variable for entry to get and set value dynamically
                 validate=None, # validate
                 vcmd=None, # vc md
                 width=24, # entry width
                 xscrollcommand=None, # scrolling command when scrolling in left-right position
                 row=0, # grid row position
                 column=0, # grid column position
                 columnspan=1, # grid column span position
                 rowspan=1, # grid row span position
                 padx=10, # grid padding left and right
                 pady=10, # grid padding top and bottom
                 ipady=2, # grid internal padding top and bottom
                 sticky='w', # grid sticky position
                 default="", # entry widget default value
                 focusinbg="bg-white", # background color when entry is focused,
                                                        # default is bootstrap referenced white
                 focusoutbg=False, # background color when entry is unfocused,
                                                        # default is False means it will set main bg again
                 focusinhlc="bg-warning", # foreground color when entry is focused,
                                                        # default is bootstrap referenced warning
                 focusouthlc=False, # foreground color when entry is unfocused,
                                                        # default is False means it will set main bg again
                 *args, **kwargs # extra arguments and keyword arguments passed
            ):

        # font style regenerate

        # font family does not change
        font_family = font[0]

        # font size is dynamic by display width
        font_size = h(font[1])-1

        # font weight getting from style
        # if it not set normal style will be applied
        font_weight = font[2] if len(font)>2 else 'normal'

        # re set all style together
        font = (font_family, font_size, font_weight)

        super(Entry, self).__init__(root,
                                    bg=color(bg), # color of background
                                    bd=bd,
                                    cursor=cursor,
                                    disabledbackground=color(dbg), # color of disable background
                                    disabledforeground=color(dfg), # color of disable foreground
                                    exportselection=eselect,
                                    font=font,
                                    fg=color(fg), # color of foreground
                                    highlightbackground=color(hlbg), # color of highlight background
                                    highlightcolor=color(hlc), # color of highlight thickness
                                    highlightthickness=hlt,
                                    insertbackground=color(ibg), # color of insert background
                                    insertborderwidth=ibd,
                                    insertofftime=iofftime,
                                    insertontime=iontime,
                                    insertwidth=iwidth,
                                    invcmd=invcmd,
                                    justify=justify,
                                    readonlybackground=color(rbg), # color of read only background
                                    relief=relief,
                                    selectbackground=color(sbg), # color of select background
                                    selectborderwidth=sbd,
                                    selectforeground=color(sfg), # color of select foreground
                                    show=show,
                                    state=state,
                                    takefocus=takefocus,
                                    textvariable=tvar,
                                    validate=validate,
                                    vcmd=vcmd,
                                    width=w(width), # responsible width by device width
                                    xscrollcommand=xscrollcommand
                                )


        # entry.grid() is automatically applied so
        # you don't need to call it again
        # just pass the grid params in entry class

        self.grid(
                row=row, # grid row position
                column=column, # grid column position
                columnspan=columnspan, # grid column span position
                rowspan=rowspan, # grid row span position
                padx=padx, # grid padding in left and right
                pady=pady, # grid padding in top and bottom
                ipady=ipady, # grid internal padding in top and bottom
                sticky=sticky # grid sticky position
            )

        # insert default value in 0 index

        self.insert(0, default)

        # set foreground color when entry is focused
        # into entry object
        # set focushighlightcolor = focusinhlc

        self.focushighlightcolor = focusinhlc

        # set background color when entry is focused
        # into entry object
        # set focusbackground = focusinbg

        self.focusbackground = focusinbg

        # set foreground color when entry is un-focused
        # into entry object
        # set focusouthighlightcolor = focusouthlc

        self.focusouthighlightcolor = focusouthlc

        # set background color when entry is un-focused
        # into entry object
        # set focusoutbackground = focusoutbg

        self.focusoutbackground = focusoutbg

        # at last set focus in background and foreground
        # in FocusIn bind

        self.bind("<FocusIn>", lambda e: self.config(
                    highlightcolor=color(focusinhlc), # color of focus in highlight color
                    bg=color(focusinbg) # color of focus in background
                )
            )

        # at last set focus out background and foreground
        # in FocusOut bind

        self.bind("<FocusOut>", lambda e: self.config(
                    highlightcolor=color(focusouthlc) if focusouthlc else color(hlbg), # color of focus out
                                # highlight color, if it set else main highlight color will be reset
                    bg=color(focusoutbg) if focusoutbg else color(bg) # color of focus out
                                # background, if it set else main background will be reset
                )
            )

        # check if text var is defined

        if tvar:

            # check if text variable value is number 0

            vl = [0, 0.0]
            if tvar.get() in vl:

                # set value automatically 0 if entry value is empty
                # else set  text var value is entry value
                # whenever time KeyRelease is happened

                self.bind("<KeyRelease>", lambda e: \
                                    tvar.set(0) if self.get() == "" \
                                        else tvar.set(self.get())
                          )

    def set(self, text=""):

        # entry.set is exactly as var.set to get extra power on entry
        # it takes one argument as text
        # this text will be replaced in entry value

        # get and set state of entry to find
        # entry state is readonly or not

        readonly = True if self['state'] == 'readonly' else False

        # check if entry state is readonly

        if readonly:

            # config readonly to normal
            # because we can't set value in a readonly entry
            # we will set readonly again after inserting

            self.config(state="normal")

        # at first delete whole text from entry widget

        self.delete(0, "end")

        # next insert text in entry box

        self.insert(0, text)

        if readonly:

            # if entry widget was readonly
            # we need to set readonly again after inserting

            self.config(state="readonly")
