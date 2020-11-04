from tkinter import Label as tkLabel
from tkinter.ttk import Label as ttkLabel
from ntk.utils import *
from PIL import Image, ImageTk

class Label(tkLabel):
    def __init__(self, root, text="New label", bg="bg-light", fg="fg-dark", var=None, case="lower", width=False, image=None, image_file=False, image_size=(32, 32), position="left", font=('Calibri', 10), row=0, column=0, rowspan=1, columnspan=1, padx=(5, 5), pady=(5, 5), ipady=10, sticky='w', length=False, *args, **kwargs):

        font = (font[0], h(font[1])-1, font[2] if len(font)>2 else 'normal')

        super(Label, self).__init__(root, textvariable=var, width=width if width else len(text), font=font, image=image, compound=position, *args, **kwargs)

        if case=="lower":
            t = text.lower()
        elif case=="upper":
            t = text.upper()
        else: t = text.capitalize()

        self.config(text=t, wraplength=length if length else len(t)*10)
        self.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, ipady=ipady, sticky=sticky)

        if image_file:
            self.img_file = Image.open(image_file)
            self.img_file = self.img_file.resize(image_size, Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.img_file)

            self.config(image=self.image, width=image_size[0]+self['width'], height=image_size[1])
