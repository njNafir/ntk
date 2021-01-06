# Import sqlite3 packages

import sqlite3

# Import global var object

from ntk.objects import gv


def row_factory(cur, row):

    # row factory function to convert all query result into dictionary object
    # it's expecting to params cursor object and result row

    # set result dictionary variable
    d = {}

    # iterate to cursor description which is containing column info
    for idx, col in enumerate(cur.description):

        # set column name = column value
        d[col[0]] = row[idx]  # result dictionary[column_name] = row_result[column]

    # return result dictionary
    return d

def connect(dbname=False, dict=True):

    # connect function is to connect to database by database name
    # connect function expecting two params dbname, dict

    # if dbname set to then it will try to connect this database
    # else it will try to connect gv.db_name

    # set connection and cursor variable None as conn, curs

    conn, curs = None, None

    try:
        conn = sqlite3.connect(
                dbname if dbname else gv.db_name, # dbname
                timeout=gv.db_timeout, # db timeout
                check_same_thread=gv.check_same_thread # check same thread or not
            )

        if dict:

            # if dictionary is true set connection row factory to custom row factory
            # then we can get dictionary object instead of tuple

            conn.row_factory = row_factory

        # get cursor object from connection object

        curs = conn.cursor()

        # set gv.database_running = True
        # we can check it in application to secure, safe and bug less result

        gv.database_running = True

    except Exception as e:

        # if we can't connect to database then we pass the function to avoid application break

        pass

    # return result connection and cursor

    return conn, curs

def disconnect(conn):

    # disconnect function is to disconnect database connection
    # disconnect function expecting exactly one param which is connection object

    try:

        # try to commit and close connection if connection is available and events is running

        # commit before close connection
        conn.commit()

        # close connection
        conn.close()

        # set gv.database_running = False
        # we can check it in application to secure, safe and bug less result

        gv.database_running = False

    except Exception as e:

        # if we can't disconnect the database connection then we pass the function to avoid application break

        pass


# add connect function to global var
# so that we can call it from everywhere where gv is available

gv.connect = connect

# add disconnect function to global var
# so that we can call it from everywhere where gv is available

gv.disconnect = disconnect
