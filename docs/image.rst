=========
ImageFile
=========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

ImageFile is a image object creator class, which can be used to automat image object creation

ntk ImageFile is extended version of tkinter base PhotoImage and Pillow Image, ImageTk, 
with more functionality, responsive grid system and with automation, to use
this ImageFile window we need to import first it from ntk by

    ``from ntk import ImageFile``

and initialize it by calling it

    ``ImageFile = ImageFile()``

This will create a ImageFile in given grid and basic style will be applied, 
you need to pass parameters described size, orient, style

available parameters are:

    * file=False, # file url
    * resize=False, # resize param is a tuple acceptable by PIL resize
    * format="png", # get and save images in this file format
    * pillow=True, # if pillow is False, ntk will be return a object which opened by tkinter PhotoImage

an example of creating ImageFile widget:


    ``from ntk import Tk, ImageFile``

    ``root = Tk(title='Example of ntk window')``

    ``image = ImageFile("C:\\Users\User\Desktop\photo.png")``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter ImageFile class.

set_image method is used by ntk ImageFile class, but you can 
use it for your purpose like set an image again after previous sets, like,

    ``image.file = "C:\\Users\User\Desktop\photo2.png"``
    ``image.set_image()``