=======
Admin
=======

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to,
good looking and os level implementation.

ntk admin utils are some os level functions which can be used to check or set program as admin mode

    ``from ntk.utils import *``

    ``admin = is_admin()`` # check if your program is running as administrator or normal

run_as_admin() function can be used to open a popup which will take permission to run as administrator and restart your program

    ``run_as_admin()``

it has three optional params

    ``python_exe=sys.executable`` # is can be passed, if you'r using multiple system at once
    ``cmdLine=None`` # is can be passed, if you want to run some cmd command by attach it to run as admin call
    ``wait=True`` # is can be passed, if want to perform wait term