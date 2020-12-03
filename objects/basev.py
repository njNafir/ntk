# Import relevant libraries
# Import global variable object

from ntk.objects import gv

# Assign base variables to use in application

def base_var():
    # base_var function can be added into custom tk object to use it in whole application

    # gv.db_name is database name to use when calling database management calls anywhere
    # It can be changed by using gv.db_name = something in application root file

    gv.db_name = "sqlite3.db"

    # gv.db_timeout is used in database connection call, by default it set to 10
    # But it can be changed by gv.db_timeout = something in application root file
    #
    # timeout is useful for database connection, because our database will be locked when query or operation is
    # mismatched for read/write call in the same cursor is running without commit
    # so the important of timeout is, whenever time our database is locked
    # database will be automatically unlocked after the timeout time

    gv.db_timeout = 10

    # gv.check_same_thread is by default set to False, but you set it to True, if your application
    # doesn't need to much database call in multi threaded environment

    gv.check_same_thread = False

    # gv.db is used by ntk backend, so you don't need to use it if you don't want to
    # dive deeper into the db backend

    gv.db = {}

    # gv.cr is also used by ntk backend, so you don't need to use it if you don't want to
    # dive deeper into the db backend

    gv.cr = {}

    # gv.cache is used by ntk backend for providing faster query, it will cache your database query result for certain
    # amount of time and when you ask for same query again if it is exists in cache
    # it will not call to database again, instead it will return cache data

    gv.cache = {}

    # gv.models is also used by ntk backend, so you don't need to use it if you don't want to
    # dive deeper into the db backend

    gv.models = {}
