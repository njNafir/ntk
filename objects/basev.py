from ntk.objects import gv

def base_var():
    gv.db_name = "sqlite3.db"
    gv.db_timeout = 10
    gv.check_same_thread = False

    gv.db = {}
    gv.cr = {}
    gv.cache = {}
    gv.models = {}
