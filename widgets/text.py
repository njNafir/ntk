# Import Tkinter Text to use it and modify default

from tkinter import Text as tkText

# Import all util from ntk.utils

from ntk.utils import *

class Text(tkText):

    # text class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # text design is custom and can be set twice
    # Text instance will contain the base tkinter text instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter text

    # so if it cause an error most probably it's getting from tkinter text object
    # see your all arguments and keywords is supporting by Text or tkinter text

    def __init__(self,
                 root, # root is a master window to place this text into it
                 sep=1, # auto separator
                 bg="bg-light", # background of text widget, default is bootstrap referenced light
                 bd=0, # border width
                 cursor="xterm", # cursor style to showing in insert position
                 eselection=1, # export selection to clipboard when text is selected
                 font=("Calibri", 10), # font style
                 fg="fg-dark", # foreground of text widget, default is bootstrap referenced dark
                 height=12, # height of text widget
                 hlbg="bg-light", # background when text widget is highlighted, default is bootstrap referenced light
                 hlc="bg-light", # foreground when text widget is highlighted, default is bootstrap referenced light
                 hlt=1, # thickness width of text when it's highlighted
                 ibg="bg-light", # background of inserted position, default is bootstrap referenced light
                 ibd=0, # insert position border width
                 iofftime=500, # insert off time for text widget
                 iontime=1000, # insert on time for text widget
                 iwidth=1, # insert position width
                 maxundo=1, # max undo with control z
                 padx=5, # grid padding left and right
                 pady=5, # grid padding top and bottom
                 relief="flat", # relief style for text widget
                 sbg="bg-primary", # background color of select background, default is bootstrap referenced primary
                 sbd=0, # select border width
                 sfg="fg-white", # foreground color of select background, default is bootstrap referenced primary
                 setgrid=0, # set grid
                 spacing1=0, # first spacing
                 spacing2=0, # second spacing
                 spacing3=0, # third spacing
                 state="normal", # text widget state
                 tabs=None, # text widget tabs
                 takefocus=1, # set if text widget can take focus or not
                 undo=1, # set undo length
                 width=48, # text widget width
                 wrap="char", # text widget wrapping method char or word
                 xscroll=None, # horizontal scroll
                 yscroll=None, # vertical scroll
                 row=0, # grid row position
                 column=0, # grid column position
                 columnspan=1, # grid column span
                 rowspan=1, # grid row span
                 sticky="w", # grid sticky position
                 tvar=False, # text variable for dynamic get and set
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        super(Text, self).__init__(root,
                                   autoseparators=sep,
                                   bg=color(bg), # color of background
                                   bd=bd,
                                   cursor=cursor,
                                   exportselection=eselection,
                                   font=font,
                                   fg=color(fg), # color of foreground
                                   height=height,
                                   highlightbackground=color(hlbg), # color of background when text widget highlighted
                                   highlightcolor=color(hlc), # color of foreground when text widget highlighted
                                   highlightthickness=hlt,
                                   insertbackground=color(ibg), # color of insert background
                                   insertborderwidth=ibd,
                                   insertofftime=iofftime,
                                   insertontime=iontime,
                                   insertwidth=iwidth,
                                   maxundo=maxundo,
                                   padx=padx,
                                   pady=pady,
                                   relief=relief,
                                   selectbackground=color(sbg), # color of select background
                                   selectborderwidth=sbd,
                                   selectforeground=color(sfg), # color of select foreground
                                   setgrid=setgrid,
                                   spacing1=spacing1,
                                   spacing2=spacing2,
                                   spacing3=spacing3,
                                   state=state,
                                   tabs=tabs,
                                   takefocus=takefocus,
                                   undo=undo,
                                   width=width,
                                   wrap=wrap,
                                   xscrollcommand=xscroll,
                                   yscrollcommand=yscroll,
                                   *args, **kwargs
                            )

        # text widget grid is automatically
        # applied so you don't need to
        # recall it again
        # instead you can pass related
        # parameters in text class

        self.grid(
                row=row, # grid row position
                column=column, # grid column position
                columnspan=columnspan, # grid column span
                rowspan=rowspan, # grid row span
                padx=padx, # grid padding left and right
                pady=pady, # grid padding top and bottom
                sticky=sticky # grid sticky position
            )

        # check if text variable is passed

        if tvar:

            # if text variable is passed

            # then set tvar.get is text.get
            # then set tvar.set is text.set

            tvar.get = self.get
            tvar.set = self.set

    def clear(self):

        # clear method is for deleting
        # all text from text widget

        self.delete(1.0, 'end')

    def get(self):

        # get method is for getting
        # all text from text widget

        return self.get(1.0, 'end')

    def set(self, text):

        # set method is to set text in text widget
        # at first it will clear field
        # and then re insert passed string to text widget

        # text.clear() is to clear full text widget

        self.clear()

        # text.insert(position, text) is used to insert text

        self.insert('end', text)
