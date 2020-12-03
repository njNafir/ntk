from tkinter import Canvas as tkCanvas
from ntk.utils import *
import pyperclip

class Canvas(tkCanvas):
    def __init__(self,
                 root,
                 bg="bg-white",
                 highlightbackground="bg-white",
                 highlightcolor="fg-dark",
                 selectbackground="bg-primary",
                 scrollregion=[0,0,350,96],
                 relief="flat",
                 width=350,
                 height=96,
                 row=0,
                 column=0,
                 rowspan=1,
                 columnspan=1,
                 padx=1,
                 pady=1,
                 mousescroll=True,
                 gridcolumn=1,
                 gridrow=1,
                 *args, **kwargs
            ):

        super(Canvas, self).__init__(root,
                                     width=width,
                                     height=height,
                                     scrollregion=scrollregion,
                                     relief=relief,
                                     background=color(bg),
                                     highlightbackground=color(highlightbackground),
                                     highlightcolor=color(highlightcolor),
                                     selectbackground=color(selectbackground),
                                     *args, **kwargs
                                )

        self.scr_x1, \
        self.scr_y1, \
        self.scr_x2, \
        self.scr_y2 = scrollregion

        self.grid(
                row=row,
                column=column,
                rowspan=rowspan,
                columnspan=columnspan,
                padx=padx,
                pady=pady
            )

        if mousescroll:
            self.bind("<MouseWheel>", lambda e: self.mousewheel(e))

        self.bind("<Double-Button-1>", lambda e: self.select_clicked(e))

        root.grid_columnconfigure(
                                    column,
                                    weight=gridcolumn
                                )

        root.grid_rowconfigure(
                                row,
                                weight=gridrow
                            )

    def select_clicked(self, e):
        if self.type("current") != "text":
            return

        self.focus_set()
        self.focus("current")
        self.select_from("current", 0)
        self.select_to("current", "end")

        self.bind("<Control-c>", lambda e: pyperclip.copy(
                                                    "{}".format(
                                                        self.selection_get()
                                                    )
                                                )
                                            )

    def mousewheel(self, e):

        self.yview_scroll(
                    int(-1*(e.delta/120)),
                    "units"
                )

    def increase_scrollragion(self, x1=False, y1=False, x2=False, y2=False):
        self.scr_x1, \
        self.scr_y1, \
        self.scr_x2, \
        self.scr_y2 = self.scr_x1 + (x1 if x1 else 0), \
                      self.scr_y1 + (y1 if y1 else 0), \
                      self.scr_x2 + (x2 if x2 else 0), \
                      self.scr_y2 + (y2 if y2 else 0)

        self.config(
                scrollregion=[
                            self.scr_x1,
                            self.scr_y1,
                            self.scr_x2,
                            self.scr_y2
                        ]
                    )

    def decrease_scrollragion(self, x1=False, y1=False, x2=False, y2=False):
        self.scr_x1, \
        self.scr_y1, \
        self.scr_x2, \
        self.scr_y2 = self.scr_x1 - (x1 if x1 else 0), \
                      self.scr_y1 - (y1 if y1 else 0), \
                      self.scr_x2 - (x2 if x2 else 0), \
                      self.scr_y2 - (y2 if y2 else 0)


        self.config(
                scrollregion=[
                            self.scr_x1,
                            self.scr_y1,
                            self.scr_x2,
                            self.scr_y2
                        ]
                    )
