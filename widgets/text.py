from ntk.utils import *
from tkinter import Text as tkText

class Text(tkText):
    def __init__(self, root, sep=1, bg="bg-light", bd=0, cursor="xterm", eselection=1, font=("Calibri", 10), fg="fg-dark", height=12, hlbg="bg-light", hlc="bg-light", hlt=1, ibg="bg-light", ibd=0, iofftime=500, iontime=1000, iwidth=1, maxundo=1, padx=5, pady=5, relief="flat", sbg="bg-primary", sbd=0, sfg="fg-white", setgrid=0, spacing1=0, spacing2=0, spacing3=0, state="normal", tabs=None, takefocus=1, undo=1, width=48, wrap="char", xscroll=None, yscroll=None, row=0, column=0, columnspan=1, rowspan=1, sticky="w", tvar=False, *args, **kwargs):

        super(Text, self).__init__(root, autoseparators=sep, bg=color(bg), bd=bd, cursor=cursor, exportselection=eselection, font=font, fg=color(fg), height=height, highlightbackground=color(hlbg), highlightcolor=color(hlc), highlightthickness=hlt, insertbackground=color(ibg), insertborderwidth=ibd, insertofftime=iofftime, insertontime=iontime, insertwidth=iwidth, maxundo=maxundo, padx=padx, pady=pady, relief=relief, selectbackground=color(sbg), selectborderwidth=sbd, selectforeground=color(sfg), setgrid=setgrid, spacing1=spacing1, spacing2=spacing2, spacing3=spacing3, state=state, tabs=tabs, takefocus=takefocus, undo=undo, width=width, wrap=wrap, xscrollcommand=xscroll, yscrollcommand=yscroll, *args, **kwargs)

        self.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, padx=padx, pady=pady, sticky=sticky)

        if tvar:
            tvar.get = self.get
            tvar.set = self.set

    def clear(self):
        self.delete(1.0, 'end')

    def get(self):
        return self.get(1.0, 'end')

    def set(self, text):
        self.clear()
        self.insert('end', text)
