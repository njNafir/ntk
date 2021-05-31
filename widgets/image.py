# Import PIL Image and ImageTk to use it

from PIL import Image as pilImage, ImageTk as pilImageTk

# Import gv object from ntk

from ntk.objects import gv

# Import os

import os

class ImageFile:

    # ImageFile class can be called once the root tk is defined
    # there is no required params but if you want
    # to have a image object you must need to pass
    # the file param value

    # other params can be set to get different type of design
    # but this is also preferred design to use in your window

    # every design is custom and can be set twice

    # init method is getting all of your arguments
    # and keyword arguments

    # so if it cause an error most probably it's getting from PIL Image ImageTk or PIL PhotoImage object
    # see your all arguments keywords and file is supporting by These tools add good formatted

    def __init__(self,
                 file=False, # file url
                 resize=False, # resize param is a tuple acceptable by PIL resize
                 format="png", # get and save images in this file format
                 pillow=True, # if pillow is False, ntk will be return a object which opened by tkinter PhotoImage
                 *args, **kwargs # extra *args and **kwargs will not be uses
            ):

        super(ImageFile, self).__init__(*args, **kwargs)

        # set pillow var into class attribute
        # so that we can call it from everywhere

        self.pillow = pillow

        # set file var into class attribute
        # so that we can call it from everywhere

        self.file = file


        # check if file url is passed

        if not self.file:

            # if file url is not passed, then it will return a default image object
            # most probably you can try and see the result
            # without having a image file

            self.file = os.path.join(gv.assets_path, "img", "default.jpg")

        # replace file url main and extension
        # so we can use it to compare

        # rsplit will split text url from right by provided splitter
        # and we are splitting whole text just once

        fnp = self.file.rsplit('.', 1)
        # fmp = self.file.rsplit(os.sep, 1)[0]

        # start to try image binding

        try:

            # at first try to set and get image
            # if there is any problem it will go to except block

            self.set_image()
        except:

            # if it came to except block
            # most probably it raising any error
            # so we can try again by saving it in a proper format

            # build a text url for file
            pngp = fnp[0] + "." + format

            # check if file path is exist
            if not os.access(pngp, os.F_OK):

                # if file path isn't exist
                # save image object into this file path

                img = pilImage.open(self.file)
                img.save(pngp, format)

            # set self.file as new image path

            self.file = pngp

            # set file extension to new format

            fnp[1] = format

        finally:

            # after everything check if resize is True

            if resize:

                # get image object to resize it

                img = pilImage.open(self.file)

                # resize image with antialias formula

                img = img.resize(resize, pilImage.ANTIALIAS)

                # at last save image object in size

                img.save(self.file, fnp[1])

            # update new image file in image object

            self.set_image()

    def set_image(self):

        # check if pillow is allowed

        if self.pillow:

            # if pillow is allowed
            # then get image object by PIL

            self.main = pilImageTk.PhotoImage(pilImage.open(self.file))

        else:

            # if pillow is not allowed
            # then get image object by tkinter PhotoImage

            self.main = PhotoImage(file=self.file)
