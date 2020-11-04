from tkinter import Button as tkButton
from ntk.utils import *

class Button(tkButton):
    def __init__(self, root, abg="bg-secondary", afg="fg-light", anchor="center", bg="bg-info", bitmap=None, bd=0, command=None, compound="left", cursor="hand2", default="normal", dfg="fg-primary", font=("Calibri", 9), fg="fg-white", height=2, hlbg="bg-light", hlc="bg-light", hlt=1, image=None, justify="center", overrelief="groove", padx=3, pady=2, relief="flat", rdelay=1000, rinterval=2000, state="normal", takefocus=1, text="Button", tvar=None, underline=99, width=16, wraplength=0, row=0, column=0, columnspan=1, ipadx=0, ipady=1, hoverbg="bg-warning", hoverfg="fg-dark", *args, **kwargs):

        super(Button, self).__init__(root, activebackground=color(abg), activeforeground=color(afg), anchor=anchor, bg=color(bg), bitmap=bitmap, bd=bd, command=command, compound=compound, cursor=cursor, default=default, disabledforeground=color(dfg), font=font, fg=color(fg), height=height, highlightbackground=color(hlbg), highlightcolor=color(hlc), highlightthickness=hlt, image=image, justify=justify, overrelief=overrelief, relief=relief, repeatdelay=rdelay, repeatinterval=rinterval, state=state, takefocus=takefocus, text=text, textvariable=tvar, underline=underline, width=width, wraplength=wraplength, *args, **kwargs)

        self.grid(row=row, column=column, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

        self.bind("<Enter>", lambda e: self.config(bg=color(hoverbg), fg=color(hoverfg)))
        self.bind("<Leave>", lambda e: self.config(bg=color(abg) if self['state'] == 'active' else color(bg), fg=color(afg) if self['state'] == 'active' else color(fg)))
