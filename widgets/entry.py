from tkinter import Entry as tkEntry
from tkinter.ttk import Entry as ttkEntry
from ntk.utils import *
from ntk.objects import gv

class Entry(tkEntry):
    def __init__(self, root, bg="bg-light", bd=0, cursor="xterm", dbg="bg-warning", dfg="fg-dark", eselect=1, font=("Calibri", 11), fg="fg-secondary", hlbg="bg-primary", hlc="fg-primary", hlt=1, ibg="bg-dark", ibd=0, iofftime=500, iontime=500, iwidth=2, invcmd="", justify="left", rbg="bg-white", relief="flat", sbg="bg-primary", sbd=2, sfg="fg-white", show=None, state="normal", takefocus=1, tvar=None, validate=None, vcmd=None, width=24, xscrollcommand=None, ttk=False, row=0, column=0, columnspan=1, rowspan=1, padx=10, pady=10, ipady=2, sticky='w', default="", focusinbg="bg-white", focusoutbg=False, focusinhlc="bg-warning", focusouthlc=False, *args, **kwargs):

        font = (font[0], h(font[1])-1, font[2] if len(font)>2 else 'normal')

        super(Entry, self).__init__(root, bg=color(bg), bd=bd, cursor=cursor, disabledbackground=color(dbg), disabledforeground=color(dfg), exportselection=eselect, font=font, fg=color(fg), highlightbackground=color(hlbg), highlightcolor=color(hlc), highlightthickness=hlt, insertbackground=color(ibg), insertborderwidth=ibd, insertofftime=iofftime, insertontime=iontime, insertwidth=iwidth, invcmd=invcmd, justify=justify, readonlybackground=color(rbg), relief=relief, selectbackground=color(sbg), selectborderwidth=sbd, selectforeground=color(sfg), show=show, state=state, takefocus=takefocus, textvariable=tvar, validate=validate, vcmd=vcmd, width=w(width), xscrollcommand=xscrollcommand)

        self.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=padx, pady=pady, ipady=ipady, sticky=sticky)
        self.insert(0, default)

        self.focushighlightcolor = focusinhlc
        self.focusbackground = focusinbg
        self.focusouthighlightcolor = focusouthlc
        self.focusoutbackground = focusoutbg

        self.bind("<FocusIn>", lambda e: self.config(highlightcolor=color(focusinhlc), bg=color(focusinbg)))
        self.bind("<FocusOut>", lambda e: self.config(highlightcolor=color(focusouthlc) if focusouthlc else color(hlbg), bg=color(focusoutbg) if focusoutbg else color(bg)))

        if tvar:
            vl = [0, 0.0]
            if tvar.get() in vl:
                self.bind("<KeyRelease>", lambda e: tvar.set(0) if self.get() == "" else tvar.set(self.get()))

    def set(self, text=""):
        readonly= True if self['state'] == 'readonly' else False

        if readonly: self.config(state="normal")
        self.delete(0, "end")
        self.insert(0, text)
        if readonly: self.config(state="readonly")
