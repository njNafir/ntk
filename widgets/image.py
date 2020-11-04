from PIL import Image as pilImage, ImageTk as pilImageTk
from ntk.objects import gv
import os

class ImageFile:
    def __init__(self, file=False, resize=False, format="png", pillow=True, *args, **kwargs):
        super(ImageFile, self).__init__(*args, **kwargs)
        self.pillow = pillow
        self.file = file

        if not self.file:
            self.file = os.path.join(gv.assets_path, "img", "default.jpg")

        fnp = self.file.rsplit('.', 1)
        fmp = self.file.rsplit(os.sep, 1)[0]

        try:
            self.set_image()
        except:
            pngp        = fnp[0] + "." + format
            if not os.access(pngp, os.F_OK):
                img     = pilImage.open(self.file)
                img.save(pngp, format)
            self.file   = pngp
            fnp[1]      = format
        finally:
            if resize:
                img     = pilImage.open(self.file)
                img     = img.resize(resize, pilImage.ANTIALIAS)
                img.save(self.file, fnp[1])

            self.set_image()

    def set_image(self):
        if self.pillow:
            self.main = pilImageTk.PhotoImage(pilImage.open(self.file))
        else:
            self.main = PhotoImage(file=self.file)
