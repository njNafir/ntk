=======
basev
=======

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to,
good looking and os level implementation.

basev stands for base variable which is used by ntk initially, but you can change it to control ntk defaults

the only function is defined here is ``base_var``, and it is

    ``def base_var():``

        ``gv.db_name = "sqlite3.db"``

        ``gv.db_timeout = 10``

        ``gv.check_same_thread = False``

        ``gv.db = {}``

        ``gv.cr = {}``

        ``gv.cache = {}``

        ``gv.models = {}``

we can change these by gv object also by 

    ``from ntk import gv``

    ``gv.db_name = "mydb"``

but for most cases we don't need to do that