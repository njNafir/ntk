import sqlite3
from ntk.objects import gv

def row_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d

def connect(dbname=False, dict=True):
    conn, curs = None, None

    try:
        conn                    = sqlite3.connect(dbname if dbname else gv.db_name, timeout=gv.db_timeout, check_same_thread=gv.check_same_thread)
        if dict: conn.row_factory        = row_factory
        curs                    = conn.cursor()
        gv.database_running     = True

    except Exception as e: pass

    return conn, curs

def disconnect(conn):
    try:
        conn.commit()
        conn.close()
        gv.database_running     = False

    except Exception as e: pass

gv.connect = connect
gv.disconnect = disconnect
