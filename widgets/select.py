from ntk.widgets.entry import Entry
from ntk.utils import *
from ntk.widgets.toplevel import Toplevel
from ntk.widgets.canvas import Canvas
from ntk.widgets.scroller import Scrollbar
from ntk.widgets.tk import Tk
from ntk.objects import gv

class SelectBox(Entry):
    def __init__(self, root, values=['Values:list/touple'], height=10, default=True, selectcommand=False, bg='#F4F4F4', onclick='', *args, **kwargs):

        super(SelectBox, self).__init__(root, bg=bg, abg=kwargs.pop('abg', bg), focusinbg=kwargs.pop('focusinbg', bg), hlbg=kwargs.pop('hlbg', bg), hlc=kwargs.pop('hlc', bg), focusinhlc=kwargs.pop('focusinhlc', bg), **kwargs)

        self.list = False
        self.height = height
        self.values = self.mvalues = values
        self.root = root
        self.selectcommand = selectcommand
        self.onclick = onclick

        setattr(gv, str(self) + ':list', False)

        self.bind("<Button-1>", lambda e: self.show_selection(e))
        self.bind('<KeyRelease>', lambda e: self.typed(e))

        if default:
            self.set(default if default != True else values[0])

    def show_selection(self, e, show=False, values=False):
        if type(values) != bool: self.values = self.mvalues = values
        if show: self.list_opened = False

        if self.onclick == 'clean':
            if e.__dict__['type'].__dict__['_name_'] == 'ButtonPress':
                self.set('')
        elif self.onclick != '':
            self.set(self.onclick)

        if not self.list:
            rx = self.winfo_rootx()
            ry = self.winfo_rooty()
            rw = self.winfo_width()
            rh = self.winfo_height()

            self.rx = rx
            self.ry = ry
            self.rw = rw
            self.rh = rh

            lv  = len(self.values)
            h   = rh*self.height if lv>self.height else rh*lv

            self.list           = Toplevel(None, x=rx, y=ry+rh, width=rw, height=h, bg='bg-white', highlightthickness=1, highlightbackground=self.focushighlightcolor, title=False)

            self.list_body      = Canvas(self.list, width=rw-2, height=h-2, scrollregion=[0,0,rw-15,h-2])

            self.list.protocol("WM_DELETE_WINDOW", self.destroy_list)

            self.list.state('withdrawn')

            self.list_opened = False

            self.update_list()

            gv.main_window.bind('<Button-1>', lambda event: self.destroy_list(event))

        elif self.list_opened:
            self.list.state('withdrawn')
            self.list_opened = False

        elif not self.list_opened:
            self.list.state('normal')
            self.list_opened = True

            self.update_list()

    def update_list(self):
        self.list_body.delete('all')

        rw = self.winfo_width()
        rh = self.winfo_height()

        for ix, v in enumerate(self.values):
            curr = 0 if v == self.get() else 1
            rct = self.list_body.create_rectangle(-2, ix*rh, rw-2, (ix+1)*rh, outline='#FAFAFA', fill=['#E9ECEF','white'][curr])
            txt = self.list_body.create_text(24*(rw/1129), ((ix+1)*rh)-(rh//2), fill=['#4c4c4c', '#4c4c4c'][curr], font=self['font'], text=str(v), anchor="w")

            self.list_body.tag_bind(rct, '<Enter>', lambda e, r=rct, t=txt: self.mouse_entered(r, t))
            self.list_body.tag_bind(rct, '<Leave>', lambda e, r=rct, t=txt: self.mouse_leaved(r, t))

            self.list_body.tag_bind(rct, '<Button-1>', lambda e, t=str(v): self.select_text(t))
            self.list_body.tag_bind(rct, '<Button-1>', lambda e, t=str(v): self.select_text(t))

            self.list_body.tag_bind(txt, '<Enter>', lambda e, r=rct, t=txt: self.mouse_entered(r, t))
            self.list_body.tag_bind(txt, '<Leave>', lambda e, r=rct, t=txt: self.mouse_leaved(r, t))

            self.list_body.tag_bind(txt, '<Button-1>', lambda e, t=str(v): self.select_text(t))
            self.list_body.tag_bind(txt, '<Button-1>', lambda e, t=str(v): self.select_text(t))

            self.list_body.config(scrollregion=[0,0,rw-15,(ix+1)*rh])

    def mouse_entered(self, ir, it):
        self.list_body.itemconfig(ir, fill="#E9ECEF")
        self.list_body.itemconfig(it, fill="#4c4c4c")

        self.list_body.config(cursor="hand2")

    def mouse_leaved(self, ir, it):
        self.list_body.itemconfig(ir, fill="white")
        self.list_body.itemconfig(it, fill="#4c4c4c")

        self.list_body.config(cursor="arrow")

    def select_text(self, t):
        self.set(t)

        self.list.destroy()
        self.list = False

        if self.selectcommand:
            self.selectcommand()

    def typed(self, e):
        tx = self.get()

        new_values = []

        for el in self.mvalues:
            if tx in el:
                new_values.append(el)

        if not new_values:
            new_values.append('No result found')

        self.values = new_values

        if type(self.list) != bool:
            self.list.destroy()
            self.list = False

        self.show_selection(e)
        self.show_selection(e)

    def destroy_list(self, e):
        ex = e.x_root
        ey = e.y_root

        if type(self.list) != bool and not (ex>self.rx and ex<(self.rx + self.rw) and \
            ey>self.ry and ey<(self.ry + self.rh)):
            self.list.destroy()
            self.list = False
