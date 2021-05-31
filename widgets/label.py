# Import Tkinter Label to use it and modify default

from tkinter import Label as tkLabel

# Import all util from ntk.utils

from ntk.utils import *

# Import Image ImageTk from PIL

from PIL import Image, ImageTk

class Label(tkLabel):

    # label class can be called once the root tk is defined
    # only one must required field is root which is the any of widget

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # every design is custom and can be set twice
    # Label instance will contain the base tkinter label instance just with modified styles and methods

    # init method is getting all of your arguments
    # and keyword arguments
    # and passing related
    # and unknown params
    # and args to tkinter frame

    # so if it cause an error most probably it's getting from tkinter label object
    # see your all arguments and keywords is supporting by Label or tkinter label

    def __init__(self,
                 root, # root is a master window to place this label into it
                 text="New label", # label text value
                 # bg="bg-light",
                 # fg="fg-dark",
                 var=None, # label text variable
                 case="lower", # text style lower upper etc
                 width=False, # label width
                 image=None, # label image
                 image_file=False, # image file to getting image object from it
                 image_size=(32, 32), # image size to getting image in custom size from image file
                 position="left", # image and text position left right center
                 font=('Calibri', 10), # label font style
                 row=0, # grid row position
                 column=0, # grid column position
                 rowspan=1, # grid row span
                 columnspan=1, # grid column span
                 padx=(5, 5), # grid padding left and right
                 pady=(5, 5), # grid padding top and bottom
                 ipady=10, # grid internal padding top and bottom
                 sticky='w', # grid sticky position
                 length=False, # label wrap length width
                 *args, **kwargs # extra arguments and keyword arguments
            ):

        # font style regenerate

        # font family does not change
        font_family = font[0]

        # font size is dynamic by display width
        font_size = h(font[1]) - 1

        # font weight getting from style
        # if it not set normal style will be applied
        font_weight = font[2] if len(font) > 2 else 'normal'

        # re set all style together
        font = (font_family, font_size, font_weight)

        # font = (font[0], h(font[1])-1, font[2] if len(font)>2 else 'normal')

        if case == "lower":

            # check if text case is lower
            # and if lower set text into lowercase

            t = text.lower()

        elif case == "upper":

            # check if text case is upper
            # and if upper set text into uppercase

            t = text.upper()

        else:

            # if text case is not lower or not upper
            # set text case into capitalize

            t = text.capitalize()

        super(Label, self).__init__(root,
                                    text=t,
                                    textvariable=var,
                                    width=width if width else len(text), # set width if width else set length of text
                                    font=font,
                                    image=image,
                                    compound=position,
                                    wraplength=length if length else len(t) * 10, # set length if length else dynamic
                                    *args, **kwargs
                                )

        # configure grid automatically
        # so you don't need to recall it again
        # just pass the grid params with label class

        self.grid(
                row=row, # grid row position
                column=column, # grid column position
                rowspan=rowspan, # grid row span
                columnspan=columnspan, # grid column span
                padx=padx, # grid padding left and right
                pady=pady, # grid padding top and bottom
                ipady=ipady, # grid internal padding top and bottom
                sticky=sticky # grid sticky position
            )

        # check if image_file is passed

        if image_file:

            # open image by PIL Image

            self.img_file = Image.open(image_file)

            # resize image by provided image size

            self.img_file = self.img_file.resize(image_size, Image.ANTIALIAS)

            # get image object from image file object

            self.image = ImageTk.PhotoImage(self.img_file)

            # re configure image object
            # re configure width from image size
            # re configure height from image size

            self.config(
                    image=self.image,
                    width=image_size[0]+self['width'],
                    height=image_size[1]
                )
