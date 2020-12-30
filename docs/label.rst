=========
Label
=========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Label is a most used text wrapping widget for tkinter

ntk Label is extended version of tkinter base Label, 
with more functionality, responsive grid system and with automation, to use
this Label window we need to import first it from ntk by

    ``from ntk import Label``

and initialize it by calling it

    ``Label = Label(root)``

This will create a Label in given grid and basic style will be applied, 
you need to pass parameters described below

available parameters are:

    * ``root``, # root is a master window to place this label into it
    * ``text="New label"``, # label text value
    * # bg="bg-light",
    * # fg="fg-dark",
    * ``var=None``, # label text variable
    * ``case="lower"``, # text style lower upper etc
    * ``width=False``, # label width
    * ``image=None``, # label image
    * ``image_file=False,`` # image file to getting image object from it
    * ``image_size=(32, 32``), # image size to getting image in custom size from image file
    * ``position="left"``, # image and text position left right center
    * ``font=('Calibri', 10)``, # label font style
    * ``row=0``, # grid row position
    * ``column=0``, # grid column position
    * ``rowspan=1``, # grid row span
    * ``columnspan=1``, # grid column span
    * ``padx=(5, 5)``, # grid padding left and right
    * ``pady=(5, 5)``, # grid padding top and bottom
    * ``ipady=10``, # grid internal padding top and bottom
    * ``sticky='w'``, # grid sticky position
    * ``length=False``, # label wrap length width

an example of creating Label widget:


    ``from ntk import Tk, Label``

    ``root = Tk(title='Example of ntk window')``

    ``image = Label(root)``

    ``root.mainloop()``

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Label class.